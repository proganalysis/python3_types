import asyncio, discord, random, re, io
from PIL import Image, ImageDraw
from .. import db

message_handlers = []

def on_message(pattern, *flags, start_only=True):
	def registrar(fn):
		message_handlers.append((re.compile(pattern, *flags), start_only, fn))
		return fn
	
	return registrar

### DAD JOKES
@on_message(r"(i'?m|((i|me)\s*(am|is|are|r|be|b)))\s+(.+)", re.IGNORECASE)
async def dad_jokes(ctx, match):
	name = ' '.join(match.group(5).split()[:4])
	if name.startswith((',', '.', '!')):
		name = name[1:].lstrip()
	response = await ctx.send('Hello **{}**, I\'m {}!', name, ctx.me)
	try:
		await ctx.bot.wait_for('message_delete', check=lambda m: m == message, timeout=60)
	except asyncio.TimeoutError:
		pass
	else:
		await response.delete()

### LONGCAT
def load(category, name):
	with open('images/%s/%s.png' % (category, name), 'rb') as f:
		im = Image.open(f)
		im.load()
		return im

cat_head, cat_body, cat_tail = (load('cat', name) for name in ('head', 'body', 'tail'))

@on_message(r'l(o+)ng\s*cat', re.IGNORECASE, start_only=False)
async def longcat(ctx, match):
	body_length = min(len(match.group(1)), 20)
	width = cat_tail.width + body_length * cat_body.width + cat_head.width
	im = Image.new('RGBA', (width, cat_head.height), 0x00000000)
	
	im.paste(cat_tail, (0, 0))
	x = cat_tail.width
	for i in range(body_length):
		im.paste(cat_body, (x, 0))
		x += cat_body.width
	im.paste(cat_head, (x, 0))
	
	buf = io.BytesIO()
	im.save(buf, 'png')
	buf.seek(0)
	await ctx.send(file=discord.File(buf, match.group(0) + '.png'))

### BRUTAL SAVAGE REKT
@on_message('brutal', re.IGNORECASE, start_only=False)
async def brutal_savage_rekt(ctx, match):
	try:
		response = await ctx.bot.wait_for('context', check=lambda c: c.channel == ctx.channel and 'savage' in c.message.content.casefold(), timeout=60)
	except asyncio.TimeoutError:
		pass
	else:
		await ctx.send('Rekt!')

### POINTING FACES
faces = (r'(☞ﾟヮﾟ)☞', r'☜(ﾟヮﾟ☜)')

@on_message('|'.join(map(re.escape, faces)), start_only=False)
async def pointing_faces(ctx, match):
	await ctx.send(faces[not faces.index(match.group(0))])

### HAT HAT HAT
@on_message(r'\bhat\s+hat\b', re.IGNORECASE, start_only=False)
async def hat_hat(ctx, match):
	await ctx.send('https://youtu.be/vyVkyakC6xk')

async def message_listener(ctx):
	if ctx.author.bot or ctx.valid:
		return
	for re, start_only, fn in message_handlers:
		# 1. Check that the message handler applies
		match = (re.match if start_only else re.search)(ctx.message.content)
		if not match: continue
		
		# 2. Check configurations to see if it's enabled and should run
		with db.Session() as session:
			guild = session.get(GuildResponses, id=getattr(ctx.guild, 'id', 0)).one_or_none()
			channel = session.get(ChannelResponses, id=ctx.channel.id).one_or_none()
			user = session.get(UserResponses, id=ctx.author.id).one_or_none()
			
			location_chance = getattr(channel, fn.__name__, None)
			if location_chance is None:
				location_chance = getattr(guild, fn.__name__, 1)  # Default to enabled
			user_chance = getattr(user, fn.__name__, 1)
		chance = location_chance * user_chance
		if not chance or random.random() > chance: continue
		
		# 3. Run the thing
		await fn(ctx, match)
		break

def setup(bot):
	bot.add_listener(message_listener, 'on_context')

response_names = tuple(fn.__name__ for _, _, fn in message_handlers)

class GuildResponses(db.DatabaseObject):
	__tablename__ = 'guild_settings'
	id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	for name in response_names:
		locals()[name] = db.Column(db.Float, nullable=False, default=1)

class ChannelResponses(db.DatabaseObject):
	__tablename__ = 'channel_settings'
	id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	for name in response_names:
		locals()[name] = db.Column(db.Float, nullable=True)

class UserResponses(db.DatabaseObject):
	__tablename__ = 'user_settings'
	id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	for name in response_names:
		locals()[name] = db.Column(db.Float, nullable=False, default=1)
