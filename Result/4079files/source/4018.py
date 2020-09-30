import json
import datetime


class libJournal:
    def __init__(self):
        self.json_location = ''

    def get_date(self):
        now = datetime.datetime.now()
        libj_date = (now.strftime("%Y-%m-%d"))
        return libj_date

    def get_time(self):
        now = datetime.datetime.now()
        libj_time = (now.strftime("%H:%M"))
        return libj_time

    def create_json(self, json_name : str):
        """Creates a json file named 'json_name'"""
        json_file_name = json_name + ".json"
        with open(json_file_name, 'xt') as f:
            f.close()

    def set_json_location(self, json_location):
        """Sets the location of the JSON used to store entries. Must be done before appending or deleting entries"""
        self.json_location = json_location

    def open_json(self, json_location):
        entries = open(json_location)
        entries_str = entries.read()
        if entries_str == '':
            entries_str = "{}"
        entries_data = json.loads(entries_str)

        return entries_data

    def add_entry(self, entry_title, content):
        """Adds an entry given title & content as long as 'json_location' has been set"""
        entries_data = self.open_json(self.json_location)

        libj_date = self.get_date()
        libj_time = self.get_time()

        entries_data[entry_title.upper()] = {"Date": libj_date, "Time": libj_time, "Content": content}

        with open(self.json_location, 'w') as fp:
            json.dump(entries_data, fp)

        print("Added entry: " + entry_title)

    def delete_entry(self, entry_title):
        """Deletes and entry given the name of the entry as long as 'json_location' has been set"""
        entries_data = self.open_json(self.json_location)

        del entries_data[entry_title.upper()]

        with open(self.json_location, 'w') as fp:
            json.dump(entries_data, fp)

        print("Deleted entry: " + entry_title)

    def read_entry(self, entry_title):
        """Searchs through all stored entries to find the one named 'entry_title'. It then returns the content"""
        entries_data = self.open_json(self.json_location)

        entry_content = entries_data[entry_title.upper()]["Content"]
        return entry_content

    def find_entry(self, entry_title):
        """Searchs through all stored entries to find the one named 'entry_title' and returns true or false"""
        entries_data = self.open_json(self.json_location)

        if entry_title.upper() in entries_data:
            print("The entry: '" + entry_title + "' is in your journal!")
            return True
        else:
            print("The entry was not found")
            return False


