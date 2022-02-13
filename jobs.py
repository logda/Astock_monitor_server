import datetime
import os

from controller import mail
from service import daily_service, stock_basic
from service.daily_analyze import zhang_ting_analyze


def zt_daily_job():
      now = datetime.datetime.now()
      daily_service.save_dayily(now)
      #stock_basic.save()
      result = zhang_ting_analyze(now)
      #os.mkdir("./data/daily/" +  str(now.strftime("%Y%m%d")))
      zt_amt_file = "./data/daily/" +  str(now.strftime("%Y%m%d")) +"/zt_amt.csv"
      zt_cnt_file = "./data/daily/" +  str(now.strftime("%Y%m%d")) +"/zt_cnt.csv"
      result[0].to_csv(zt_amt_file)
      result[1].to_csv(zt_cnt_file)
      mail.send(zt_amt_file, zt_cnt_file)
      
      

if __name__ == '__main__':
      zt_daily_job()