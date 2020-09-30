""" Session Module for Instagram"""
import time

import random
import requests


class Session(object):
    """
    Session class to handle authentication.
    """
    accept_language = 'en-US,en;q=0.8,pt-br,pt;q=0.6,'
    user_agent = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')

    def __init__(self, username, password, logging=None):
        from src.instabot import URL
        self.URL = URL
        self.user_login = username.lower()
        self.user_password = password
        self.session = requests.Session()
        self.logging = logging
        self.login_status = False
        self.login_post = {}
        self.csrftoken = None

    def __del__(self):
        if self.login_status:
            self.logout()

    def login(self):
        """
        login method to login to Instagram
        :return:
        """
        self.log('User: %s --> Login attempt...' % self.user_login)
        self.session.cookies.update({
            'sessionid': '',
            'mid': '',
            'ig_pr': '1',
            'ig_vw': '1920',
            'csrftoken': '',
            's_network': '',
            'ds_user_id': ''
        })
        self.login_post = {
            'username': self.user_login,
            'password': self.user_password
        }
        self.session.headers.update({
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': self.accept_language,
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': self.user_agent,
            'X-Instagram-AJAX': '1',
            'X-Requested-With': 'XMLHttpRequest'})
        request = self.session.get(self.URL['root'])
        self.session.headers.update({'X-CSRFToken': request.cookies['csrftoken']})
        time.sleep(random.randint(2, 5))
        login = self.session.post(self.URL['login'], data=self.login_post, allow_redirects=True)
        self.session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        self.csrftoken = login.cookies['csrftoken']
        time.sleep(random.randint(2, 5))
        if login.status_code == 200:
            request = self.session.get(self.URL['root'])
            finder = request.text.find(self.user_login)
            if finder != -1:
                self.login_status = True
                self.log('User: %s --> Successful login!' % self.user_login)
            else:
                self.log('Wrong username or password.')
        else:
            self.log('Wrong username or password.')

    def logout(self):
        """
        Logout method to logout from Instagram
        :return:
        """
        try:
            logout_post = {'csrfmiddlewaretoken': self.csrftoken}
            logout = self.session.post(self.URL['logout'], data=logout_post)
            self.log("Successful logout!")
            self.log(logout.status_code)
            self.login_status = False
        except Exception as logout_exception:
            self.log(logout_exception)
            self.log("Error: Unsuccessful logout.")

    def post(self, url):
        """
        Post to URL
        :param url:
        :return:
        """
        response = self.session.post(url)
        self.log("POST request to: " + url + " - Status: " + str(response.status_code))
        return response.status_code

    def log(self, text):
        """
        Generic Logger
        :param text:
        :return:
        """
        if self.logging:
            self.logging.info(text)
