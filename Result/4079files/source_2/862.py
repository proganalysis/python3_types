import sys

def check_version():
	version = sys.version_info[:3]
	if version >= (3, 5):
		return True
	else:
		log.error('Excalibot requires Python 3.5+. This is version ' + ('%d.' * 3) % version)
		log.error('Please update Python and run excalibot again.')
		return False

def run_excalibot():
	import json, pkgutil
	from . import Excalibot, db, log, config
	
	log.debug('Creating bot')
	bot = Excalibot(config.bot_config)
	
	log.debug('Loading extensions')
	for _, cog, _ in pkgutil.iter_modules(['excalibot/cogs']):
		if cog == 'utils': continue
		log.debug('Loading extension %s', cog)
		bot.load_extension('excalibot.cogs.' + cog)
	
	db.DatabaseObject.metadata.create_all()
	
	bot.run()
	
	bot.loop.close()
	log.shutdown()

if check_version():
	run_excalibot()
