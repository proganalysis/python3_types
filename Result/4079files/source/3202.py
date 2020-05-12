from urllib import request, parse, error
from http import cookiejar
from html.parser import HTMLParser
from .exceptions import VKAuthError
import re
import json


class Api:

    def __init__(self, v_api, token=None, expires_in=None, user_id=None):
        self.token = token
        self.expires_in = expires_in
        self.user_id = user_id
        self.v_api = v_api

    def auth(self, app_id, scope, login, password):
        opener = request.build_opener(request.HTTPCookieProcessor(cookiejar.CookieJar()), request.HTTPRedirectHandler())

        try:
            response_auth = opener.open("https://oauth.vk.com/authorize?client_id={}"
                                        "&display=page&redirect_uri=https://oauth.vk.com/blank.htm&scope={}"
                                        "&response_type=token&v={}".format(app_id, scope, self.v_api))
        except error.HTTPError:
            raise VKAuthError("Don't auth, may be wrong app id")

        parser = AuthFormParser()
        parser.feed(str(response_auth.read()))
        parser.close()

        parser.params['email'] = login
        parser.params['pass'] = password

        response_allow = opener.open(parser.url, parse.urlencode(parser.params).encode('utf8'))
        url_parse = parse.urlparse(response_allow.geturl())

        if url_parse.path != '/blank.html':
            query = parse.parse_qs(url_parse.query)
            if 'email' in query:
                raise VKAuthError("Wrong login or pass")
            action_allow = re.findall(r'(?<=<form\smethod=\"post\"\saction=\").*(?=\")', response_allow.read()
                                      .decode("utf-8"))[0]
            response_allow = opener.open(action_allow)
            url_parse = parse.urlparse(response_allow.geturl())

        query_params = dict((k, v) for k, v in (item.split('=') for item in url_parse.fragment.split('&')))
        self.token = query_params['access_token']
        self.expires_in = query_params['expires_in']
        self.user_id = query_params['user_id']

    def call_method(self, method: str, params: dict):
        url = "https://api.vk.com/method/{}?{}&access_token={}&v={}".format(method, parse.urlencode(params),
                                                                            self.token, self.v_api)
        response = request.urlopen(url).read().decode('utf-8')
        return json.loads(response)


class AuthFormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.url = None
        self.params = {}
        self._in_form = False
        self._form_parsed = False
        self.method = "GET"

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "form":
            if self._form_parsed:
                raise RuntimeError("Second form on page")
            if self._in_form:
                raise RuntimeError("Already in form")
            self._in_form = True
        if not self._in_form:
            return
        attrs = dict((name.lower(), value) for name, value in attrs)
        if tag == "form":
            self.url = attrs['action']
            if "method" in attrs:
                self.method = attrs['method']
        elif tag == "input" and "type" in attrs and "name" in attrs:
            if attrs["type"] in ["hidden", "text", "password"]:
                self.params[attrs["name"]] = attrs["value"] if "value" in attrs else ""

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "form":
            if not self._in_form:
                raise RuntimeError("Unexpected end of <form>")
            self._in_form = False
            self._form_parsed = True

    def error(self, message):
        pass
