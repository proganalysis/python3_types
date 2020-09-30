import json, os.path
from collections.abc import Mapping, MutableMapping

_file = 'config.json'

class Config(MutableMapping):
	def __init__(self, **kwargs):
		self._values = {}
		self.update(kwargs)
	
	def __getitem__(self, key):
		return self._values[key]
	
	def __setitem__(self, key, value):
		if isinstance(value, Mapping):
			value = Config(**value)
		self._values[key] = value
	
	def __delitem__(self, key):
		del self._values[key]
	
	def __iter__(self):
		yield from self._values
	
	def __len__(self):
		return len(self._values)
	
	def populate(self, values):
		for key, value in values.items():
			if key not in self._values: continue # Automatically delete removed settings
			default = self._values[key]
			if isinstance(default, Config) and isinstance(value, Mapping):
				default.populate(value)
			else:
				self._values[key] = value
	
	def to_dict(self):
		"""Create a standard dictionary with the same values as myself (primarily for creating JSON)."""
		dict_ = dict(self)
		for k, v in dict_.items():
			if isinstance(v, Config):
				dict_[k] = v.to_dict()
		return dict_
	
	def __str__(self):
		return dict.__str__(self)
	
	def __repr__(self):
		return '<Config {0._values}>'.format(self)

config = Config(default_prefix = '<', prefix_check = True,
	github = Config(username = None, repository = None, branch = 'master'),
	auto_reload = Config(webhook_channel = None, webhook_id = None),
	auth = Config(discord_token = None, tba_token = None),
	status = 'online',
	activity = Config(name = "@{client.user!s} what's your prefix? | {guild_count} guilds", type = 0, url = None)
)

if os.path.isfile(_file):
	with open(_file) as f:
		config.populate(json.load(f))

with open(_file, 'w') as f:
	json.dump(config.to_dict(), f, indent='\t')
