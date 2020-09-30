import requests
import os
import json
from datetime import date as get_date
from datetime import datetime
import time

# 날짜가 2014-2-5이 첫 게시글이 있는 날짜이고,
# 2014-2-1202를 2017-5-17로 계산하는 특성을 이용해봤습니다


class Crawler:
    # bamboo_tuple : (id, nickname)
    # id = 대숲 id(fbpage.kr 사이트의 pi 파라미터)
    # nickname = 대숲 별칭(데이터를 저장할 폴더명이며, 임의로 설정가능)

    # 15 - CAU bamboo               => 2014-2-5 ~
    # 142 - CAU dark bamboo         => 2015-4-14 ~

    mypath = os.path.abspath(os.path.dirname(__file__))
    notExistDays = set()

    # 헤더
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
        'Connection': 'keep-alive',
        'Content-Length': '52',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'PHPSESSID=qc745ke67p76ut4q8j29h8jst0',
        'Host': 'cau.fbpage.kr',
        'Origin': 'http://cau.fbpage.kr',
        'Referer': 'http://cau.fbpage.kr/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1165 '
    }


    # Constructor
    def __init__(self, bamboo_tuple, first_date):
        self.bamboo_id = bamboo_tuple[0]
        self.bamboo_nickname = bamboo_tuple[1]
        self.first_date = first_date
        self.first_day = int(first_date.split('-')[-1])

    # 날짜로 데이터 받아오기
    def getDataWithDate(self, date, page):
        data = {"mode": "list", "searchType": 3, "page": page, "keyword": date}

        res = requests.post("http://cau.fbpage.kr/ajax.php?pi=" + str(self.bamboo_id), json=data, headers=self.headers)

        time.sleep(0.1)

        return res.json()

    # content 저장
    def writeContent(self, post_num):
        i = 0
        while True:
            i += 1

            try:
                data = open(os.path.join(self.mypath + '/' + self.bamboo_nickname + '/json',
                                         str(i) + '.txt'), "r")
                posting = json.loads(data.read())
                data.close()

                # 파일 작성
                if not os.path.exists(self.mypath + '/' + self.bamboo_nickname + '/data'):
                    os.mkdir(self.mypath + '/' + self.bamboo_nickname + '/data')

                if not os.path.exists(self.mypath + '/' + self.bamboo_nickname + '/data' + '/' + "-".join(posting['date'].split()[:3])):
                    os.mkdir(self.mypath + '/' + self.bamboo_nickname + '/data' + '/' + "-".join(posting['date'].split()[:3]))

                with open(os.path.join(self.mypath + '/' + self.bamboo_nickname + '/data',
                                       "-".join(posting['date'].split()[:3]) + '/' + str(post_num) + '.txt'), "w") as file1:
                    file1.write(posting['date'] + '\n')
                    file1.write(posting['content'])
                print(post_num)
                post_num += 1
            except FileNotFoundError:  # 파일이 더이상 없으면 종료
                print("*********************")
                print("Done!")
                break

    # JSON 데이터 저장(날짜별로 폴더 생성)
    def writeJSON(self, day, post_num):
        page = 1

        # 첫 포스팅일부터 오늘까지의 일 수 구하기
        now = datetime.now()
        delta = get_date(now.year, now.month, now.day) \
                - get_date(int(self.first_date.split('-')[0]), int(self.first_date.split('-')[1]), self.first_day)

        while True:
            postings = self.getDataWithDate(self.first_date.split('-')[0] + "-"
                                            + self.first_date.split('-')[1] + "-"
                                            + str(day), page)['request']['data']
            if len(postings) == 0:
                if day > self.first_day + delta.days:  # 오늘을 넘어설 때
                    break

                if page == 0:
                    self.notExistDays.add(day)

                page = 1
                day += 1
                continue
            page += 1

            for posting in postings:
                # 파일 작성
                if not os.path.exists(self.mypath + '/' + self.bamboo_nickname):
                    os.mkdir(self.mypath + '/' + self.bamboo_nickname)

                if not os.path.exists(self.mypath + '/' + self.bamboo_nickname + '/json'):
                    os.mkdir(self.mypath + '/' + self.bamboo_nickname + '/json')

                with open(os.path.join(self.mypath + '/' + self.bamboo_nickname + '/json',
                                       str(post_num) + '.txt'), "w", encoding='utf-8') as file:
                    json.dump(posting, file)

                print(post_num)
                post_num += 1
        print("*********************")
        print("Done!")
        print("Empty date Set: " + str(self.notExistDays))
        return day, post_num


if __name__ == '__main__':

    cau = Crawler((15, 'CAU'), '2014-2-5')

    cau.writeContent(1)
