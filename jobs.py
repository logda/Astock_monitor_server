import datetime

import daily_zhangTing_analysis
from config import Configure_storer 
from mail_senter import send_mail

def input_data_zt_analyze():
  print('=======')
  print(datetime.date.today())
  config_storer = Configure_storer('./config/config.yml')
  date = enter_date()
  df = daily_zhangTing_analysis.get_daystock(date ,config_storer.data['tushare_api'])
  print(df.head())


def today_zt_analyze():
  print('=======')
  current = (datetime.datetime.now())
  print(current)
  config_storer = Configure_storer('./config/config.yml')
  file1, file2 = daily_zhangTing_analysis.daily_zt_analyze(current ,config_storer.data['tushare_api'])
  send_mail(file1, file2, config_storer.data)


if __name__ == '__main__':
  today_zt_analyze()
  from apscheduler.schedulers.blocking import BlockingScheduler
  scheduler = BlockingScheduler()
  scheduler.add_job(today_zt_analyze, 'cron', day_of_week='mon-fri', hour='16', minute=0)
  scheduler.start()
