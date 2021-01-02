import datetime

import daily_zhangTing_analysis
from config import Configure_storer 
from mail_senter import send_mail
def main():
  print('=======')
  print(datetime.date.today())
  config_storer = Configure_storer('./config/config.yml')

  file1, file2 =daily_zhangTing_analysis.run(str(datetime.date.today()),config_storer.data['tushare_api'])
  send_mail(file1, file2, config_storer.data)
if __name__ =='__main__':
  main()
  
