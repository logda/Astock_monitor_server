#!/usr/bin/env python
# coding: utf-8

import tushare as ts
import pandas as pd

import sys
import os

def get_daystock(date, key):
  pro = ts.pro_api(key)
  df = pro.daily(trade_date=date)
  return df

def run(today, key):  
  #today = str(datetime.date.today())
  today = today.replace('-','')
  file_path = './data/' + today + '_Astock.csv'
  #today = '20200703'
  if os.path.exists(file_path):
    print('Day data already exit.')
    df = pd.read_csv(file_path)
  else:
    df = get_daystock(today, key)
    df.to_csv(file_path)

  print(df)
  gb_file_name_01 = today + '_hangye_count_gb.csv'
  gb_file_name_02 = today + '_hangye_amt_gb.csv'
  #__今日涨停的股票__
  ZhangTing_df = df[(df["pct_chg"]>9.5) & (df["pct_chg"]<10.5) ]
  print(ZhangTing_df.head())

  #__行业字典___
  HangYe_df = pd.read_excel('./data/2020-02-07_ALL.xlsx', encoding='utf-8')
  #print(HangYe_df.head())

  #HangYe_df['ts_code']= HangYe_df["股票代码"].map(lambda x:str(x)[:-3])
  ZhangTing_df['ts_code'] = ZhangTing_df['ts_code'].apply(str)
  HangYe_df['ts_code'] = HangYe_df['股票代码'].apply(str)
  temp = pd.merge(ZhangTing_df, HangYe_df, how="inner",
                on="ts_code")

  temp = temp[['股票代码', '股票简称', '所属同花顺行业',"amount"]]
  temp['成交量'] = temp[['amount']].apply(lambda x:x/100000000)
  hangye_count_gb = temp.groupby(['所属同花顺行业'])
  #print(hangye_count_gb['amount'].agg(['count', 'sum']))
  hangye_count_gb = (hangye_count_gb['amount'].agg(['count']).sort_values(by='count', ascending=False))
  hangye_count_gb.to_csv('./data/'+gb_file_name_01)
  print(hangye_count_gb.head())

  hangye_amt_gb = temp.groupby(['所属同花顺行业'])
  hangye_amt_gb = (hangye_amt_gb['成交量'].agg(['sum']).sort_values(by='sum', ascending=False))
  #hangye_amt_gb = hangye_amt_gb.sort_values(ascending=False, inplace=True)
  hangye_amt_gb.to_csv('./data/'+gb_file_name_02)
  print(hangye_amt_gb.head())
  print()
  print('Success dumped 2 file: {},{}'.format(gb_file_name_01, gb_file_name_02))
  return gb_file_name_01, gb_file_name_02
  #import ZhangTing_sent_mail
  #ZhangTing_sent_mail.send_mail(gb_file_name_01, gb_file_name_02)
