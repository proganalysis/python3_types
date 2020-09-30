# coding=utf-8
import sqlite3
import os
import os.path
import hashlib
import time
import requests

log = open("log.txt", "w")
file = "test.sq3"
connexion = sqlite3.connect(file)
cursor = connexion.cursor()
current = os.getcwd() + "\\data"

print("<CreatingDatabase>files</CreatingDatabase>")
cursor.execute("CREATE TABLE files (file TEXT, directory TEXT, hash TEXT, action TEXT, size INT)")


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def parse(path, file):
    s = ('<SelectedFile>' + path + "\\" + file + "</SelectedFile>")
    ##    print(s)
    log.write(s + '\n')
    rel_path = path[len(current):]
    d = os.path.join(path, file)
    hash_value = md5(d)
    ######################
    # time_created = int(os.path.getctime(path+"\\"+file))7
    size = str(os.path.getsize(d))
    action = "DLL"
    s = ('DATA ||| name:' + file + ' || PATH:' + rel_path + ' || HASH :' + hash_value +
         '|| size : ' + size)

    log.write(s)

    if is_in_table(rel_path, file):
        s = ('[Existing=True]')
        log.write(s + '\n')
        update_file(rel_path, file, hash_value, action, size)
    else:
        s = ('[Existing=False]')
        log.write(s + '\n')
        add_file(rel_path, file, hash_value, action, size)


def is_in_table(path, file):
    cursor.execute("SELECT * FROM files WHERE file='" + file + "' AND directory='" + path + "'")
    data = list(cursor)
    if len(data) > 0:
        return True
    else:
        return False


def update_file(path, file, hash_value, action, size):
    s = ("<Update>" + file + "</Update>")
    ##    print(s)
    log.write(s + '\n')
    cursor.execute("SELECT * FROM files WHERE file='" + file + "' AND directory='" + path + "'")
    data = list(cursor)[0]
    if data[2] != hash_value:
        cursor.execute(
            "UPDATE files SET hash='" + hash_value + "' WHERE file='" + file + "' AND directory='" + path + "'")
        cursor.execute(
            "UPDATE files SET action='" + action + "' WHERE file='" + file + "' AND directory='" + path + "'")
        cursor.execute("UPDATE files SET size='" + size + "' WHERE file='" + file + "' AND directory='" + path + "'")
    connexion.commit()


def add_file(path, file, hash_value, action, size):
    s = ('<AddingFile>' + file + '</AddingFile>')
    ##    print(s)
    log.write(s + '\n')
    cursor.execute(
        "INSERT INTO files(file,directory,hash,action,size) VALUES('" + file + "','" + path + "','" + hash_value + "','" + action + "','" + size + "')")
    connexion.commit()


def analyse(path):
    s = ('<CurrentDir>' + path + '</CurrentDir>')
    ##    print(s)
    log.write(s + '\n')
    for sub in os.listdir(path):
        # time.sleep(0.5)
        if os.path.isfile(path + "\\" + sub):
            parse(path, sub)
        else:
            analyse(path + "\\" + sub)


analyse(current)

connexion.commit()

cursor.close()
connexion.close()
log.close()
