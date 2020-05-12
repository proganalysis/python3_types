#! python3

import os
import platform
from importlib import reload

import schedule

import augentbot


def connect_run() -> None:
    os.system('git pull')
    if platform.system() == 'Windows':
        os.system('chcp 65001')  # fixes encoding errors on windows
    reload(augentbot)
    augentbot.run(create_buffers=1)


if __name__ == '__main__':
    schedule.every().day.at('00:59').do(connect_run)
    schedule.every().day.at('01:59').do(connect_run)
    schedule.every().day.at('02:59').do(connect_run)
    schedule.every().day.at('03:59').do(connect_run)
    schedule.every().day.at('04:59').do(connect_run)
    schedule.every().day.at('05:59').do(connect_run)
    schedule.every().day.at('06:59').do(connect_run)
    schedule.every().day.at('07:59').do(connect_run)
    schedule.every().day.at('08:59').do(connect_run)
    schedule.every().day.at('09:59').do(connect_run)
    schedule.every().day.at('10:59').do(connect_run)
    schedule.every().day.at('11:59').do(connect_run)
    schedule.every().day.at('12:59').do(connect_run)
    schedule.every().day.at('13:59').do(connect_run)
    schedule.every().day.at('14:59').do(connect_run)
    schedule.every().day.at('15:59').do(connect_run)
    schedule.every().day.at('16:59').do(connect_run)
    schedule.every().day.at('17:59').do(connect_run)
    schedule.every().day.at('18:59').do(connect_run)
    schedule.every().day.at('19:59').do(connect_run)
    schedule.every().day.at('20:59').do(connect_run)
    schedule.every().day.at('21:59').do(connect_run)
    schedule.every().day.at('22:59').do(connect_run)
    schedule.every().day.at('23:59').do(connect_run)

    while True:
        schedule.run_pending()
