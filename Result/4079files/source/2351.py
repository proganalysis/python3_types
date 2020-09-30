from tinify import tinify, ServerError, ClientError, ConnectionError
import os
from configobj import ConfigObj

conf_file = './birb_prefs'


def get_files(folder):
    files_found = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isdir(path):
            files_found.extend(get_files(path))
        elif os.path.isfile(path):
            size = os.path.getsize(path)
            files_found.append((size, path))
    return files_found

config = ConfigObj(conf_file)
images_folder = config['images_folder']
tinify_key = config["tinify_key"]

if tinify_key is None or tinify_key is '' or tinify_key == '-':
    print("No tinify key given")
else:
    tinify.key = tinify_key
    files = get_files(images_folder)

    files.sort(key=lambda s: -s[0])

    try:
        for pair in files:
            print("tinifying file: {} - size before: {} - size after: ".format(pair[1], pair[0]), end='')

            try:
                source = tinify.from_file(pair[1])
                source.to_file(pair[1])
                print(os.path.getsize(pair[1]))
            except ClientError as er:
                print("Client Error while tinifying: {}".format(er))
            except ServerError as er:
                print("Server Error while tinifying: {}".format(er))
            except ConnectionError as er:
                print("Connection Error while tinifying: {}".format(er))

    except tinify.AccountError as e:
        print("Account Error while tinifying: {}".format(e))
