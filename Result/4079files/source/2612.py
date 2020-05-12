#!/usr/bin/python3
'''
Created on Apr 24, 2017

@Author: frederich River
@Project: Venus
@Workflow:
    1.generate a total list.
    2.compare with database, remove the codes already exist.
    3.
    4.
@Version:
v1.0.2-beta, Apr 5, 2018
find a critical bug that if no table created in stock data,
system will also treat the stock as exist.
'''
import functools
from libbase import *
from libmysql8 import MySQLServer
import libencrypt
import time

__version__ = '1.0.1-beta'

INDEX_DB = 'finance'
STOCK_DATA_DB = 'stock_data'

def stocklist(flag='all'):
    '''
    stocks: stocks only
    indexs: indexs only
    sh: stocks in sh only
    sz: stocks in sz only
    a: A stock only sh & sz
    b: B stock only sh & sz
    hk: stocks in hongkong
    zxb: ZXB only
    cyb: CYB only
    funds: funds only
    '''
    indexs = []
    sha = ['SH600000']*4000
    for i in range(len(sha)):
        sha[i] = 'SH' + '60' + str(i).zfill(4)
    indexs.extend(sha)
    sza = ['SZ000001']*1000
    for i in range(len(sza)):
        sza[i] = 'SZ' + str(i).zfill(6)
    indexs.extend(sza)
    cyb = ['SZ300001']*1000
    for i in range(len(cyb)):
        cyb[i] = 'SZ' + '300' + str(i).zfill(3)
    indexs.extend(cyb)
    zxb = ['SZ002000']*1000
    for i in range(len(zxb)):
        zxb[i] = 'SZ' + '002' + str(i).zfill(3)
    indexs.extend(zxb)
    szb = ['SZ200001']*1000
    for i in range(len(szb)):
        szb[i] = 'SZ' + '200' + str(i).zfill(3)
    indexs.extend(szb)
    shi = ['SH000000']*2000
    for i in range(999):
        shi[i] = 'SH' + str(i).zfill(6)
        shi[i + 1000] = 'SH' + '950' + str(i).zfill(3)
    indexs.extend(shi)
    szi = ['SZ399000']*1000
    for i in range(len(szi)):
        szi[i] = 'SZ' + '399' + str(i).zfill(3)
    indexs.extend(szi)

    if flag == 'all':
        indexs.extend(sha)
        indexs.extend(sza)
        indexs.extend(shi)
        indexs.extend(szi)
    elif flag == 'stocks':
        indexs.extend(sha)
        indexs.extend(sza)
    elif flag == 'a':
        indexs.extend(sha)
        indexs.extend(sza)
    elif flag == 'b':
        indexs.extend(shb)
        indexs.extend(szb)
    elif flag == 'zxb':
        indexs.extend(zxb)
    elif flag == 'cyb':
        indexs.extend(cyb)
    elif flag == 'hk':
        indexs.extend(hk)
    else:
        pass
    return indexs

def querylist(db, tab):
    """
    db: database of 'indexs'
    tab: table of db
    today: date of today which is a 8bit integer.
    ---
    Return:
    result: a list type object which contains codes of stocks.
    """
    index_list = db.SELECTVALUES(tab=tab, col='stock_code')
    result = []
    for index in index_list:
        if db.TABLEEXIST(index[0]):
            result.append(index[0])
    return result

"""
Two partial functions used for querying indexs and stocks.
"""
queryindex = functools.partial(querylist, tab= 'stock_index')

def stockinfo(code, tab, db_index, db_rec, today):
    """     x: stock index which is in format of 'SH600001'
            tab: table name which is 'indexs.stocks'
            db1: database of 'indexs'
            db2: database of 'stock_data'
            today: today is a integer in format of 8 integer numbers.
    """
    """    from config read url of 'http://money.163.com'    """
    url_ne_index = readurl('URL_NE_INDEX')
    query_index = neteaseindex(code)
    print(url_ne_index)
    netease_stock_index_url = url_ne_index.format(query_index, today)
    try:
        result = opencsv(netease_stock_index_url, 'gb18030')
        if len(result) > 0:
            print(code, result.iloc[1, 2])
            stock_name = result.iloc[1, 2].replace(' ', '')
            content = databasedef('DEF_INDEX')
            db_rec.CREATETABLE(code, content)
            db_index.INSERTVALUE(tab,
                                  "stock_code,stock_name,gmt_modified",
                                  "'%s','%s','%s'" % (code,
                                      stock_name,time2str()))
    except Exception as e:
        err('Searching index error: %s' % e)
        time.sleep(10)
    return 1

def updatedata():
    querydb = MySQLServer(acc='stock',
                          pw='stock2018',
                          database=INDEX_DB)
    recdb = MySQLServer(acc='root',
                        pw='6414939',
                        database=STOCK_DATA_DB)
    stock_list = queryindex(querydb)
    for stock in stock_list:
        fetch_stock(querydb, recdb, STOCK_DATA_DB, stock, date2str2())

def createstock(stock_list):
    querydb=MySQLServer(acc='stock',
                        pw='stock2018',
                        database=INDEX_DB)
    createdb = MySQLServer(acc='root',
                           pw='6414939',
                           database=STOCK_DATA_DB)
    for stock in stock_list:
        stockinfo(stock,'stock_index',querydb,createdb,date2str2())

def nonlisted(gen_list):
    '''
    This function generate a list of stock indexs.
    For Shanghai is SHxxxxxx.
    For Shenzhen is SZxxxxxx.
    -----
    Returns:
        new_list: a char type list object
    '''
    querydb = MySQLServer(acc='stock',
                          pw='stock2018',
                          database=INDEX_DB)
    old_list = queryindex(querydb)
    new_list = []
    for index in gen_list:
        if index not in old_list:
            new_list.append(index)
    return new_list

def fetch_stock(db_index,db_rec,tab,code,today):
    """
    1.Get stock data from www.163.com.
    2.Write data into database.
    3.Update a global table to record update history.
    ---
    It is an event and returns nothing.
    """
    infolog('Update %s'% code)
    print(code)
    url_ne_stock = readurl('URL_NE_STOCK')
    query_index = neteaseindex(code)
    '''get start date from query update time'''
    '''#update = db_index.selectOne(tab, 'gmt_modified', "stock_code='%s'"%
    index)[-1]'''
    start_time = '19901219'
    end_time = '20180405'
    netease_stock_index_url = url_ne_stock.format(
            query_index, start_time,end_time)
    try:
        result = opencsv(netease_stock_index_url, 'gb18030')
        if len(result):
            result.replace('None',0.0)
            for i in range(0,result.shape[0])[::-1]:
                query_date=result.iloc[i,0]
                CP=result.iloc[i,3]
                HP=result.iloc[i,4]
                LP=result.iloc[i,5]
                OP=result.iloc[i,6]
                YCP=result.iloc[i,7]
                AMP=result.iloc[i,9]
                VolT=result.iloc[i,10]
                ValT=result.iloc[i,11]
                if db_rec.SELECTVALUES(code,'*',"trade_date='%s'"% query_date)==():
                    try:
                        columns='trade_date,close_price,high_price,\
                                low_price,open_price,\
                                yesterday_close_price,\
                                amplitude,turn_volumn,turn_value'
                        content="'%s',%s,%s,%s,%s,%s,%s,%s,%s"\
                        % (query_date,CP,HP,LP,OP,YCP,AMP,VolT,ValT)
                        db_rec.INSERTVALUE(code,columns, content)
                    except Exception as e:
                        err('Inserting error when fetching stocks: %s' % e)
                else:
                    try:
                        content='close_price=%s,high_price=%s,\
                                low_price=%s,open_price=%s,\
                            yesterday_close_price=%s,amplitude=%s,\
                            turn_volumn=%s,turn_value=%s'\
                             %(CP, HP,LP,OP,YCP,AMP,VolT,ValT)
                        db_rec.UPDATETABLE(code, content, "trade_date='%s'"\
                                % query_date)
                    except Exception as e:
                        err('Updating error when fetching stocks: %s' % e)
                db_index.UPDATETABLE(tab, "gmt_modified='%s'" % query_date,
                        "stock_index='%s'" % code)
    except Exception as e:
        err('Downloading error when opening stock data: %s' % e)


def query_stock_list():
    """
    Querying stock codes from database.
    Used to seperate account from query process.
    Return: a list of stock codes.
    """
    querydb = MySQLServer(acc='stock',
                          pw='stock2017',
                          database=INDEX_DB)
    return query_stock(querydb)

if __name__ == '__main__':
    #updatedata()
    print('TEST START!')
    temp_list = stocklist(flag = 'all')
    print(temp_list[:10])
    ms = MySQLServer('stock', libencrypt.mydecrypt('wAKO0tFJ8ZH38RW4WseZnQ=='), 'finance')
    print(querylist(ms, 'stock_index')[:15])
    non_listed_stock = nonlisted(temp_list)
    print(non_listed_stock[20])
    createstock(non_listed_stock)
