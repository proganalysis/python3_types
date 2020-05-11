import asyncio
import ssl
import json
from urllib.parse import urlparse, urlencode, quote

from rain.cythons.tcpio import TCPIo, Packet
from rain.cythons.form import MultiDict, QueryDict
from rain.cythons.cookies import Cookies

from copy import deepcopy

_loop = None


def get_loop():
	global _loop

	if _loop is None:
		_loop = asyncio.get_event_loop()

	return _loop


def set_loop(loop: asyncio.AbstractEventLoop):
	global _loop
	_loop = loop


class RequestTimeoutException(Exception):
	pass


class Environment(object):
	def __init__(self, query: MultiDict = None, data=None, headers: MultiDict = None):
		self.query = MultiDict()
		if query:
			self.query.update(query)

		self.data = data
		self.headers = MultiDict({'User-Agent': 'API:Client', 'Connection': 'Close'})
		if headers:
			self.headers.update(headers)

	def copy(self):
		return Environment(
			deepcopy(self.query), deepcopy(self.data), deepcopy(self.headers)
		)


class ClientResponse(object):
	# noinspection PyTypeChecker
	def __init__(self):
		self.status: int = 200
		self.reason: str = 'OK'
		self.header: MultiDict = None
		self._body: bytes = None
		self.cookies: Cookies = None

	@property
	def json(self):
		return json.loads(self._body)

	@property
	def txt(self):
		return self._body.decode()

	@property
	def raw(self):
		return self._body


async def fetch(
	method: str, url: str,
	query: dict = None, data=None,
	headers: dict = None, env: Environment = None,
	loop: asyncio.AbstractEventLoop = None,
	timeout: float = -1
) -> ClientResponse:
	if loop is None:
		loop = get_loop()

	method = method.upper()

	env = env.copy() if env else Environment()

	if query:
		env.query.update(query)

	if data:
		if isinstance(data, dict):
			env.data.update(data)
		else:
			env.data = data

	if headers:
		env.headers.update(headers)

	_ = urlparse(url)

	is_https = False
	scheme = _.scheme.lower()
	if scheme not in ['http', 'https']:
		raise ValueError(f'Error Url: {url}')
	if scheme == 'https':
		is_https = True

	port = 443 if is_https else 80

	host = _.netloc

	if ':' in host:
		*_h, port = host.split(':')
		host = ':'.join(_h)
		port = int(port)

	path = quote(_.path or '/')

	query = QueryDict.load(_.query) or QueryDict()
	env.query.update(query)
	query_string = urlencode(query, doseq=True)
	if query_string:
		query_string = '?' + query_string

	_ssl = ssl.create_default_context() if is_https else None

	conn = TCPIo(*await asyncio.open_connection(host, port, ssl=_ssl, loop=loop))

	data = None
	if method in {'POST', 'PUT'}:
		data = env.data

		if isinstance(data, dict):
			if env.headers.get('Content-Type') == 'json/application':
				_ = json.dumps(data, ensure_ascii=False, indent=0, separators=(',', ':')).encode()
			else:
				env.headers['Content-Type'] = 'application/x-www-form-urlencoded'
				_ = urlencode(data, doseq=True).encode()
		else:
			_ = data if isinstance(data, bytes) else str(data).encode()

		# noinspection PyTypeChecker
		env.headers['Content-Length'] = len(_)

	conn.writer.write('{} {}{} HTTP/1.0\r\n'.format(method.upper(), path, query_string).encode())
	conn.writer.write(
		'\r\n'.join(
			map(lambda x: ': '.join(map(str, x)), env.headers.items())
		).encode() + b'\r\n\r\n'
	)
	if data:
		conn.writer.write(_)
	conn.writer.write(b'\r\n')

	if timeout < 0:
		return await _read_response(conn)

	future = asyncio.Future()

	task = loop.create_task(_task_wrapper(future, conn))
	handler = loop.call_later(timeout, _timeout_handler, future, task)
	await future
	handler.cancel()

	if future.exception():
		raise future.exception()
	return future.result()


async def _task_wrapper(future, conn):
	await asyncio.sleep(2)
	rv = await _read_response(conn)
	future.set_result(rv)


def _timeout_handler(future, task):
	if future.done():
		return
	future.set_exception(RequestTimeoutException())
	task.cancel()


async def _read_response(conn: TCPIo):
	res = ClientResponse()

	line = (await conn.reader.readuntil()).rstrip().decode()
	v, status, *reason = line.split(' ')

	res.status = int(status)
	res.reason = ' '.join(reason)
	res.cookie = {}

	header = {}
	while True:
		line = (await conn.reader.readuntil()).rstrip().decode()
		if not line:
			break

		ind = line.find(':')
		if ind < 0:
			continue

		key = line[:ind]
		val = line[ind + 1:].strip()

		if key == 'Set-Cookie':
			cookie_item = {}
			ckv, *c_attrs = val.split('; ')
			c_k, *c_v = ckv.split('=')

			cookie_item['name'] = c_k
			cookie_item['value'] = '='.join(c_v)
			for c_attr in c_attrs:
				ind = c_attr.find('=')
				if ind > -1:
					cookie_item[c_attr[:ind]] = c_attr[ind + 1:]
				else:
					cookie_item[c_attr] = True

			res.cookie[c_k] = cookie_item

		header[key] = val

	res.header = header

	length = int(header.get('Content-Length', -1))
	if length > 0:
		p = Packet()
		await conn.read_to_packet(p, length)
		res._body = p.getvalue()
	elif length < 0:
		res._body = await conn.reader.read()
	else:
		res._body = b''

	return res


if __name__ == '__main__':
	res = asyncio.get_event_loop().run_until_complete(fetch("get", "http://www.baidu.com", timeout=1))
	print(res)
