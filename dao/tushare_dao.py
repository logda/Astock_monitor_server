#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts 

token = ""
pro = ts.pro_api(token)

def get_daily(trade_date):
    df = pro.daily(trade_date = str(trade_date.strftime("%Y%m%d")))
    return df

def get_stock_basic():
    df = pro.query('stock_basic', exchange='', list_status='L',
                   fields='ts_code,symbol,name,area,industry,list_date')
    return df
