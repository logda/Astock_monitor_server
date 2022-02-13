import datetime

import daily_zhangTing_analysis
from config import Configure_storer 
from mail_senter import send_mail

from service import daily_service, stock_basic
from service.daily_analyze import zhang_ting_analyze

def main():
  print('=======')
  print(datetime.datetime.now())
  config_storer = Configure_storer('./config/config.yml')
  now = datetime.datetime.now()
  file1, file2 = daily_zhangTing_analysis.daily_zt_analyze(now,config_storer.data['tushare_api'])
  send_mail(file1, file2, config_storer.data)

def main2():
      now = datetime.datetime.now()
      daily_service.save_dayily(now)
      #stock_basic.save()
      
      zhang_ting_analyze(now)
      
if __name__ =='__main__':
      main2()
  
