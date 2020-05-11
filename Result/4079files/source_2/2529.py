from http import HTTPStatus as BuiltinHTTPStatus

MaxContentLength = 3 * 1024 * 1024

DateTimeFormat = '%Y-%m-%d %H:%M:%S'


class _ContentType(object):
	pass


class ContentTypes(object):
	JSON = object()
	TEXT = object()
	FROM = object()
	MULTI_PART = object()
	UNSUPPORTED = object()

	@classmethod
	def content_type(cls, name):
		return {
			'text/html': cls.TEXT,
			'text/xml': cls.TEXT,
			'text/plain': cls.TEXT,
			'text/json': cls.JSON,
			'application/json': cls.JSON,
			'application/x-www-form-urlencoded': cls.FROM,
			'multipart/form-data': cls.MULTI_PART,
		}.get(name, cls.UNSUPPORTED)

	@classmethod
	def supported(cls, name):
		return cls.content_type(name) is not cls.UNSUPPORTED


_http_all_attrs = dict(
	map(
		lambda x: (str(x.value), (x.name.replace('_', ' '), x.phrase.encode())),
		map(
			lambda x: getattr(BuiltinHTTPStatus, x),
			filter(lambda x: x.isupper(), dir(BuiltinHTTPStatus))
		)
	)
)

_http_all_attrs['lookup'] = classmethod(lambda cls, status: getattr(cls, str(status), None))

HTTPStatus = type(
	'HTTPStatus',
	(object,),
	_http_all_attrs
)
