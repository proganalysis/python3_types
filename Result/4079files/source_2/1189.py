from config import Configure


class IntranetAPI:
    """
    Simple AutoLogin API
    """

    def __init__(self, config):
        if not isinstance(config, Configure):
            raise TypeError("Invalid instance of Configure")
        if config.get_auto_login() == "None":
            raise ValueError("Please check auth key")
        self._config = config
        self._host = "https://intra.epitech.eu/"
        self._format = "json"
        self._auth = None

    def get_host(self):
        return self._host

    def get_config(self):
        return self._config

    def get_format(self):
        return self._format

    def set_host(self, host):
        self._host = host

    def set_config(self, config):
        self._config = config

    def set_format(self, format):
        self._format = format

    def url_formated(self, middle):
        return self._host + self._config.get_auto_login() + "/" + middle + "?format=" + self._format

    def url_formated_with_user(self, middle, login):
        return self._host + self._config.get_auto_login() + "/user/" + login + "/" + middle + "?format=" + self._format
