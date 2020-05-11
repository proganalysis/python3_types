import sqlite3
import datetime


class libJournal:
    def __init__(self):
        """
        :rtype: object
        """
        self.db_location = ''
        self.entry_number = 0

    @staticmethod
    def __get_date():
        now = datetime.datetime.now()
        libj_date = (now.strftime("%Y-%m-%d"))
        return libj_date

    @staticmethod
    def __get_time():
        now = datetime.datetime.now()
        libj_time = (now.strftime("%H:%M"))
        return libj_time

    def set_db_location(self, db_name: str):
        """
        Sets location of the database. Must be done as used globally through all methods
        :param db_name:
        :return:
        """
        self.db_location = db_name

    @staticmethod
    def create_db(db_name: str):
        """
        Creates a new database
        :param db_name:
        :return:
        """
        conn = sqlite3.connect(db_name + ".db")
        conn.close()

    @staticmethod
    def setup_db (db_name: str):
        """
        Formats (or sets up) an existing SQL database
        :param db_name:
        :return:
        """
        conn = sqlite3.connect(db_name + ".db")
        c = conn.cursor()
        try:
            c.execute('''CREATE TABLE entries
                        (number PRIMARY KEY, title text, date text, time text, content text)''')
        except sqlite3.OperationalError as e:
            print("You have already formatted this database!")
            print(e)

        conn.commit()
        conn.close()

    def __set_latest_entry_number(self):
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()

        entry_number = []

        for row in c.execute('SELECT * FROM entries ORDER BY number'):
            entry_number.append(row[0])

        self.entry_number = len(entry_number) + 1

    def entry_new(self, entry_title: str, entry_content: str):
        """
        Creates a new entry
        :param entry_title:
        :param entry_content:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()

        date = self.__get_date()
        time = self.__get_time()

        self.__set_latest_entry_number()

        db_entry = (self.entry_number, entry_title, date, time, entry_content)
        c.execute('''INSERT INTO entries(number, title, date, time, content)
                          VALUES(?,?,?,?,?)''', db_entry)

        conn.commit()
        conn.close()

        self.entry_number = self.entry_number + 1

    def entries_all(self):
        """
        Returns all entries
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()
        c.execute("SELECT * FROM entries")

        rows = c.fetchall()
        # for row in rows:
        #     print(row)

        return rows

    def most_recent_entry(self):
        """
        Will return data from the most recent entry.
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()
        c.execute("SELECT * FROM entries")

        most_recent_entry = c.fetchall()
        # print(most_recent_entry[-1])
        return most_recent_entry[-1]

    @staticmethod
    def __entries_iterate(entry_dict):
        y = 0
        for x in entry_dict:
            a = ''.join(str(x))
            z = str(y)
            # print(z + ": " + a)
            y = y+1

    def search_by_title(self, entry_title: str):
        """
        Searches for all entries with the name, and returns a list of entries & returns all the entries numbered
        :param entry_title:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()

        c.execute('SELECT * FROM entries WHERE title="{title}"'.format(title=entry_title))
        entries_found = c.fetchall()

        self.__entries_iterate(entries_found)
        return entries_found

    def search_by_date(self, entry_date: str):
        """
        Searches for all entries with the date, and returns a list of entries & returns all the entries numbered
        :param entry_date:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()
        c.execute('SELECT * FROM entries WHERE date="{date}"'.format(date=entry_date))
        entries_found = c.fetchall()

        self.__entries_iterate(entries_found)

        return entries_found

    def search_by_number(self, entry_number: int):
        """
        Searches for specific entry with entry_number, and returns the entry
        :param entry_number:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()
        c.execute('SELECT * FROM entries WHERE number={number}'.format(number=entry_number))
        entries_found = c.fetchall()

        # print(entries_found)
        return entries_found

    def read_by_title(self, entry_name: str, entry_location: int):
        """
        Returns data for specific entries based on title, and location if multiple. Sorted by most recent to oldest
        :param entry_name:
        :param entry_location:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()

        c.execute('SELECT * FROM entries WHERE title="{title}"'.format(title=entry_name))
        entries_found = c.fetchall()
        entry_specified = entries_found[entry_location][-1]

        # print(entry_specified)
        return entry_specified

    def read_by_date(self, entry_date: str, entry_location : int):
        """
        Returns data for specific entries based on date, and location if multiple. Sorted by most recent to oldest
        :param entry_date:
        :param entry_location:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()

        c.execute('SELECT * FROM entries WHERE date="{date}"'.format(date="entry_date"))
        entries_found = c.fetchall()
        entry_specified = entries_found[entry_location][-1]

        # print(entry_specified)
        return entry_specified

    def read_by_number(self, entry_number: int):
        """
        "Returns data for specific entries based on entry_number
        :param entry_number:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()

        c.execute('SELECT * FROM entries WHERE number="{number}"'.format(number=entry_number))
        entry_found = c.fetchall()
        entry_specified = entry_found[-1]

        # print(entry_specified)
        return entry_specified

    def delete_by_number(self, entry_number: int):
        """
        Deletes an entry based on it's entry_number
        :param entry_number:
        :return:
        """
        conn = sqlite3.connect(self.db_location)
        c = conn.cursor()

        c.execute('DELETE FROM entries WHERE number="{number}"'.format(number=entry_number))


