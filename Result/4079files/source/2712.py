import datetime
import io
import json
import logging
import time

import requests

from modules import Exceptions
from modules import Utils


class Model:

    def __init__(self, username, autoupdate=True):
        """

        :param username: The username to create a model instance of
        :param autoupdate: Automatically update model variables when accessed if older than 10 seconds since last update
        """
        self._response = None
        self.__model_image = None
        self.__online = None
        self.__status = None
        self.last_update = None
        self.username = username
        self.autoupdate = autoupdate

    @property
    def status(self):
        if self.__status is None:
            self.update_model_status()
            return self.__status
        elif (datetime.datetime.now() - self.last_update).total_seconds() > 10 and self.autoupdate:
            self.update_model_status()
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def online(self):
        if self.__online is None:
            self.update_model_status()
            return self.__online
        elif (datetime.datetime.now() - self.last_update).total_seconds() > 10 and self.autoupdate:
            self.update_model_status()
        return self.__online

    @online.setter
    def online(self, value):
        self.__online = value

    @property
    def model_image(self):
        if self.autoupdate:
            self.update_model_image()
        try:
            self.__model_image.seek(0)  # see https://bit.ly/2YtCQ7e
        except AttributeError:
            return None
        else:
            return self.__model_image

    @model_image.setter
    def model_image(self, value):
        self.__model_image = value

    def update_model_status(self):
        """
        Updates self.online and self.status
        """
        for attempt in range(5):
            # noinspection PyBroadException
            try:
                self.last_update = datetime.datetime.now()
                target = f"https://en.chaturbate.com/api/chatvideocontext/{self.username}"
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36', }
                self._response = requests.get(target, headers=headers)

                if "Cloudflare is currently unable to resolve your requested domain" in str(self._response.content):
                    self._response = None
                    raise ConnectionError
                elif "The web server reported a bad gateway error." in str(self._response.content):
                    self._response = None
                    raise ConnectionError
                elif "Cloudflare is unable to establish an SSL connection" in str(self._response.content):
                    self._response = None
                    raise ConnectionError
                elif "The web server is not returning a connection" in str(self._response.content):
                    self._response = None
                    raise ConnectionError
            except Exception:
                logging.info(self.username + " has failed to connect on attempt " + str(attempt))
                time.sleep(3)  # sleep and retry
            else:
                break

        if self._response is None:
            logging.info(self.username + " has failed to connect after all attempts")
            self.status = "error"

        elif b"It's probably just a broken link, or perhaps a cancelled broadcaster." in self._response.content:  # check if models still exists
            self.status = "canceled"

        elif self._response.status_code == 401:
            self._response = json.loads(self._response.content)
            if "Room is deleted" in str(self._response['detail']):
                self.status = "deleted"
            elif "This room has been banned" in str(self._response['detail']):
                self.status = "banned"
            elif "This room is not available to your region or gender." in str(self._response['detail']):
                self.status = "geoblocked"
            elif "This room requires a password" in str(self._response['detail']):
                self.status = "password"
            else:
                self.status = "error"

        elif self._response.status_code == (200 and 401):
            logging.error(f'{self.username} got a {self._response.status_code} error')
            self.status = "error"

        else:
            try:
                self._response = json.loads(self._response.content)
            except Exception as e:
                Utils.handle_exception(e)
                logging.critical("This response should have been json decodable")
                try:
                    logging.critical(str(self._response.content))
                except Exception as e:
                    Utils.handle_exception(e)
                    logging.critical("The response could not be printed")
                self.status = "error"
            else:
                self.status = self._response["room_status"]

        if self.status in {"offline", "error", "deleted", "banned", "geoblocked", "canceled"}:
            self.online = False
        else:
            self.online = True

    def update_model_image(self):
        """
        Updates self.image


        :raise ModelOffline if self.status is 'offline'
        :raise ModelAway if self.status is 'away'
        :raise ModelPrivate if self.status is 'private' or 'hidden'
        :raise ModelPassword if self.status is 'password'
        :raise ModelDeleted if self.status is 'deleted'
        :raise ModelBanned if self.status is 'banned'
        :raise ModelGeoblocked if self.status is 'geoblocked'
        :raise ModelCanceled if self.status is 'canceled'
        :raise ModelNotViewable if any other error happens
        """
        if self.online and self.status not in {"away", "private", "hidden", "password"}:
            attempt_count = 0
            for attempt in range(5):
                try:
                    data = requests.get(f'https://roomimg.stream.highwebmedia.com/ri/{self.username}.jpg').content
                    bio_data = io.BytesIO(data)
                    self.model_image = bio_data
                except Exception as e:
                    Utils.handle_exception(e)
                    attempt_count += 1
                    logging.info(self.username + " has failed to obtain image on attempt " + str(attempt))
                    time.sleep(1)  # sleep and retry
                else:
                    break
            if attempt_count == 5:
                logging.info(self.username + " has failed to obtain image after all attempts")
                raise ConnectionError
        elif self.status == "offline":
            raise Exceptions.ModelOffline
        elif self.status == "away":
            raise Exceptions.ModelAway
        elif self.status in {"private", "hidden"}:
            raise Exceptions.ModelPrivate
        elif self.status == "password":
            raise Exceptions.ModelPassword
        elif self.status == "deleted":
            raise Exceptions.ModelDeleted
        elif self.status == "banned":
            raise Exceptions.ModelBanned
        elif self.status == "geoblocked":
            raise Exceptions.ModelGeoblocked
        elif self.status == "canceled":
            raise Exceptions.ModelCanceled
        else:
            raise Exceptions.ModelNotViewable
