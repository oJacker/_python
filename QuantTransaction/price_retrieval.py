#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import print_function

import datetime
import warnings

import MySQLdb as mdb
import requests

# Obtain a databases conncetion to the Mysql instance
db_host ='localhost'
db_user = 'root'
db_pass = '123456'
db_name = 'securities'
con = mdb.connect(db_host,db_user,db_pass,db_name)


def obtain_list_of_db_tickers():
    """
    Obtains a list of the ticker symbols in the database.
    :return:
    """
    with con:
        cur = con.cursor()
        cur.execute("SELECT id , ticker, FROM symbol")
        data = cur.fetchall()
    return [(d[0], d[1]) for d in data]

def get_daily_historic_data_yahoo(ticker, start_date=(2014,1,1), end_date=datetime.date.today().timetuple()[0:3]):
    """
    Obtains data from Yahoo Finance returns and a list of tuples.
    ticker: Yahoo Finace ticker symbol,e.g "GOOG" from Goole, Inc. start_date:Start date in (YYY,M, D) fromat
    end_date: End date in (YYYY, M , D) format
    :param ticker:
    :param start_date:
    :param end_date:
    :return:
    """
    #Construct the Yahoo URL with the correct integer query parameters
    #for start and end dates. Note that some parameters are zero-based!

    ticker_tup = (
        ticker, start_date[1] - 1, start_date[2],
        start_date[0], end_date[1] - 1, end_date[2],
        end_date[0]
    )