import datetime


def generate_dev_version(version):
    if 'dev' in version:
        version = '.'.join(version.split('.')[:-1])
    now = datetime.datetime.now()
    time_string = (str(now.year) + str(now.month) + str(now.day) + str(now.hour) +
                   str(now.minute) + str(now.second))
    return version + '.dev' + time_string
