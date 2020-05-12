#!/usr/bin/python3
"""
Geschafen im Aug 31, 2017

Verfasst von Friederich Fluss

Lib of mysql contains methods to drive mysql db using python.
v1.0.0-stable: Library is released.
v1.0.1-stable: Encrypted password is supported, relative codes are in
libencrypt.
v1.0.2-stable: Add new function TABLEEXIST.
v2.0.3-dev: Complete funcions of mysql.
v2.0.4-dev: Modify some bug, using encrypt pw.
v2.0.5-dev: Fix bug. drop table -> drop table if exists.
"""

"""
X2.exit
4.grant db to user
X7.drop database
X9.use database
X10.select now
15.delete from table where
17.multi table update
*18.alter table add index
20.alter table add unique index
25.rename table
26.database backup
"""
import sys
sys.path.append('..')
from applications.libencrypt import mydecrypt
from applications.libbase import info, warning, err
import pymysql

__version__ = '2.0.5-dev'
#encode = 'wAKO0tFJ8ZH38RW4WseZnQ=='


class MySQLBase(object):
    def __init__(self, acc, pw, database,
                 host='localhost', charset='utf8'):
        self.db = pymysql.connect(host=host, user=acc,
                                  passwd=pw, db=database, charset=charset)
        self.cs = self.db.cursor()
        self.version = self._version()

    def _version(self):
        self.cs.execute('select Version()')
        self.db.commit()
        return self.cs.fetchone()[0]

    def create_database(self, dbName):
        sql = 'create database {0}'.format(dbName)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            info('MySQL database creation failure: %s' % e)
            return 0

    def drop_database(self, dbName):
        sql = 'drop database if exists {0}'.format(dbName)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            info('MySQL database delete failure: %s' % e)
            return 0

    def create_table(self, tabName, content):
        sql = 'create table if not exists {0} ({1})'.format(
            tabName, content)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            err(sql)
            info('MySQL table creation failure: %s' % e)
            return 0

    def update_table(self, tabName, content, condition):
        sql = 'update {0} set {1} where {2}'.format(tabName,
                                                    content, condition)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            info('MySQL table updating failure: %s' % e)
            return 0

    def insert_all_values(self, tabName, content):
        sql = 'insert into {0} values({1})'.format(
            tabName, content)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            info('MySQL inserting failure: %s' % e)
            return 0

    def insert_value(self, tabName, field, content):
        sql = 'insert into {0} ({1}) values({2})'.format(
            tabName, field, content)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            err(sql)
            info('MySQL inserting failure: %s' % e)
            return 0

    def select_values(self, tabName, field, *args):
        try:
            if args != ():
                sql = 'select {0} from {1} where {2}'.format(
                    field, tabName, args[0])
                self.cs.execute(sql)
            else:
                sql = 'select {0} from {1}'.format(
                    field, tabName)
                self.cs.execute(sql)
            return self.cs.fetchall()
        except Exception as e:
            info('MySQL selecting failure: %s' % e)
            return None

    def select_one(self, tabName, field, condition):
        sql = 'select {0} from {1} where {2}'.format(field, tabName, condition)
        try:
            self.cs.execute(sql)
            return self.cs.fetchone()
        except Exception as e:
            info('MySQL selecting failure: %s' % e)
            return None

    def add_column(self, tab, col, col_type, *args):
        try:
            if args:
                sql = 'alter table {0} add {1} {2} default {3}'
                sql = sql.fotmat(tab, col, col_type, args[0])
                self.cs.execute(sql)
            else:
                sql = 'alter table {0} add {1} {2}'
                sql = sql.format(tab, col, col_type)
                self.cs.execute(sql)
            return 1
        except Exception as e:
            info('MySQL adding column failure: %s' % e)
            return 0

    def add_index(self, tab):
        sql = 'alter {0} '
        try:
            return 1
        except Exception as e:
            return 0

    def drop_index(self, tab_name, idx_name):
        sql = 'alter {0} drop index {1}'.format(
            tab_name, idx_namei)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            info('MySQL drop index failure: %s' % e)
            return 0

    def add_primary_key(self, tab_name, idx_name):
        sql = 'alter table {0} add primary key {1}'.format(
            tab_name, idx_name)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            info('MySQL add primary key failure: %s' % e)
            return 0

    def change_column(self, tabName, old_name, new_name, new_type):
        sql = 'alter table {0} change {1} {2} {3}'.format(
            tabName, old_name, new_name, new_type)
        try:
            self.cs.execute(sql)
            return 1
        except Exception as e:
            info('MySQL change column failure: %s' % e)
            return 0

    def drop_column(self, tabName, fieldName):
        sql = 'alter table {0} drop {1}'.format(
            tabName, fieldName)
        try:
            self.cs.execute(sql)
            return 1
        except Exception as e:
            info('MySQL drop column failure: %s' % e)
            return 0

    def remove_data(self, table_name, condition):
        sql = 'delete from {0} Where {1}'.format(
            table_name, condition)
        try:
            self.cs.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            info('MySQL delete failure: %s' % e)
            return 0

    def show_databases(self):
        try:
            self.cs.execute("show databases")
            self.db.commit()
            return self.cs.fetchall()
        except Exception as e:
            info('MySQL database showing failure: %s' % e)
            return 0

    def show_tables(self):
        try:
            self.cs.execute("show tables")
            self.db.commit()
            return self.cs.fetchall()
        except Exception as e:
            info('MySQL table showing failure: %s' % e)
            return 0

    def table_exists(self, table_name):
        try:
            sql = "select table_name \
                    from information_schema.TABLES \
                    where table_name='{0}'"
            self.cs.execute(sql.format(table_name))
            self.db.commit()
            return self.cs.fetchone()
        except Exception as e:
            info('MySQL table checking failure: %s' % e)
            return 0

    def drop_table(self, table_name):
        try:
            sql = "drop table if exists {0}".format(table_name)
            self.cs.execute(sql)
            self.db.commit()
        except Exception as e:
            info('MySQL table dropping failure: %s' % e)
            return 0

if __name__ == '__main__':
    ms = MySQLBase('stock', mydecrypt(encode), 'finance')
    print(ms)
