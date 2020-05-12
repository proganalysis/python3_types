from default_imports import *
from conf.ConfigWrapper import ConfigWrapper as ConfigWrapper
from pymongo import MongoClient
from pymongo.database import Database as Database

class DBManager:
    def client(self) -> MongoClient: ...
    def db(self) -> Database: ...
