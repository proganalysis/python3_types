from rain import Rain, View

from examples.mysql.main import client

app = Rain()


@app.register("/")
class View(View):
	async def get(self):
		async with client.connctx() as conn:
			lst = (await conn.query("select * from account_user")).lst

		return self.jsonify({'users': lst})


if __name__ == '__main__':
	app.run(ACCESS_LOGGING=False)
