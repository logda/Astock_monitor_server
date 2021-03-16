import datetime

import daily_zhangTing_analysis
from config import Configure_storer 
from mail_senter import send_mail


def main():
  print('=======')
  print(datetime.datetime.now())
  config_storer = Configure_storer('./config/config.yml')
  now = datetime.datetime.now()
  file1, file2 = daily_zhangTing_analysis.daily_zt_analyze(now,config_storer.data['tushare_api'])
  send_mail(file1, file2, config_storer.data)


if __name__ =='__main__':
  main()
  
