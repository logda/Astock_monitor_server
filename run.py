import datetime

import daily_zhangTing_analysis
from config import Configure_storer 
from mail_senter import send_mail


def enter_date():
  date = input("enter date you wanna to anlayze (YYYY-MM-DD)\n")
  date = date.split('-')
  if len(date) == 3:
    return str(datetime.date(int(date[0]), int(date[1]), int(date[2])))   
  else:
    print('date format error')
    enter_date()


def today_zt_analyze():
  print('=======')
  current = (datetime.datetime.now())
  print(current)
  config_storer = Configure_storer('./config/config.yml')
  file1, file2 = daily_zhangTing_analysis.daily_zt_analyze(current ,config_storer.data['tushare_api'])
  send_mail(file1, file2, config_storer.data)


if __name__ =='__main__':
  today_zt_analyze()
  
