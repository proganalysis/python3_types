import copy

from configmaster import exc


class ConfigKey(object):
    """
    A ConfigKey object is a collection that is stored via class attributes.

    >>> d = {"a": 2, "b": [1, 2, {"c": 3}], {"d": 4}}
    >>> config = ConfigKey.ConfigKey()
    >>> config.load_from_dict(d)
    >>> config.a # Returns 2
    >>> config.b[1] # Returns 2
    >>> config.b[3] # Returns a new ConfigKey, as it's a dict.

    ConfigKeys take in data from dicts, and set attributes of themselves to accommodate the items inside the dictionaries.
    There are special cases for handling lists, and all objects inside a list are automatically parsed appropriately, with dicts turning into ConfigKeys.

    If the item begins with "__" OR is in the list of the ConfigKey keywords, it has the "unsafe_" prefix added to it, unless safe_load is False.
    If the item has a '.' in it, it is replaced with a '_'
    """
    def __init__(self, safe_load: bool=True):
        self.parsed = False
        self.safe_load = safe_load

    def __iter__(self):
        ndict = copy.copy(self.__dict__)
        ndict.pop('parsed')
        ndict.pop('safe_load')
        return ndict.__iter__()

    def __contains__(self, item):
        # Sigh.
        return item in self.__dict__

    def dump(self) -> dict:
        """
        Dumps data from the ConfigKey into a dict.
        :return: The keys and values from the ConfigKey encapsulated in a dict.
        """
        d = {}
        for item in self.__dict__:
            if item in ['parsed', 'dump', 'parse_data', 'iter_list', 'safe_load']:
                continue
            if isinstance(self.__dict__[item], ConfigKey):
                d[item] = self.__dict__[item].dump()
            elif isinstance(self.__dict__[item], list):
                d[item] = self.iter_list_dump(self.__dict__[item])
            else:
                d[item] = self.__dict__[item]
        return d


    def items(self):
        ndict = copy.copy(self.__dict__)
        ndict.pop('parsed')
        ndict.pop('safe_load')
        return ndict.items()

    def keys(self):
        ndict = copy.copy(self.__dict__)
        ndict.pop('parsed')
        ndict.pop('safe_load')
        return ndict.keys()

    def values(self):
        ndict = copy.copy(self.__dict__)
        ndict.pop('parsed')
        ndict.pop('safe_load')
        return ndict.values()

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def load_from_dict(self, data: dict, overwrite: bool=True):
        """
        Loads key/values from dicts or list into the ConfigKey.
        :param data: The data object to load.
                        This can be a dict, or a list of key/value tuples.
        :param overwrite: Should the ConfigKey overwrite data already in it?
        """
        if data is None or data == {}:
            return False
        # Loop over items
        if isinstance(data, list) or isinstance(data, tuple):
            # Pick a random item from the tuple.
            if len(data[0]) != 2:
                raise exc.LoaderException("Cannot load data with length {}".format(len(data[0])))
            items = data
        elif isinstance(data, dict) or isinstance(data, self.__class__):
            items = data.items()
        else:
            raise exc.LoaderException("Cannot load data of type {}".format(type(data)))
        for key, item in items:
            assert isinstance(key, str)
            if hasattr(self, key) and not overwrite:
                # Refuse to overwrite existing data.
                continue
            # Check name to verify it's safe.
            if self.safe_load:
                if key.startswith("__") or key in ['dump', 'items', 'keys', 'values',
                                                   'iter_list', 'load_from_dict', 'iter_list_dump',
                                                   'parsed', 'safe_load']:
                    # It's evil!
                    key = "unsafe_" + key
            if '.' in key:
                # Doubly evil!
                key = key.replace('.', '_')
            if isinstance(item, dict):
                # Create a new ConfigKey object with the dict.
                ncfg = ConfigKey()
                # Parse the data.
                ncfg.load_from_dict(item)
                # Set our new ConfigKey as an attribute of ourselves.
                setattr(self, key, ncfg)
            elif isinstance(item, list):
                # Iterate over the list, creating ConfigKey items as appropriate.
                nlst = self.iter_list(item)
                # Set our new list as an attribute of ourselves.
                setattr(self, key, nlst)
            else:
                # Set the item as an attribute of ourselves.
                setattr(self, key, item)
        # Flip the parsed flag,
        self.parsed = True

    def iter_list(self, data: list):
        l = []
        for item in data:
            if isinstance(item, list):
                l.append(self.iter_list(item))
            elif isinstance(item, dict):
                ncfg = ConfigKey()
                ncfg.load_from_dict(item)
                l.append(ncfg)
            else:
                l.append(item)
        return l

    def iter_list_dump(self, data: list):
        l = []
        for item in data:
            if isinstance(item, list):
                l.append(self.iter_list_dump(item))
            elif isinstance(item, ConfigKey):
                l.append(item.dump())
            else:
                l.append(item)
        return l