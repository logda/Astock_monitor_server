
import os

from dao import tushare_dao
from common import path_util


def save_dayily(date):    
  file_path = path_util.get_daily_path(date)
  if os.path.exists(file_path):
    print('Local data alreay exist')
  else:
    print('Local data not exist, get form Dao')
    df = tushare_dao.get_daily(trade_date=date)
    print('/'.join(file_path.split("/")[:-1]))
    os.makedirs('/'.join(file_path.split("/")[:-1]))
    df.to_csv(file_path)
    