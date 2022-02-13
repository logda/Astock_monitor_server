
from dao import tushare_dao
from common import path_util

def save():
    save_path = path_util.get_stock_basic_path()
    df = tushare_dao.get_stock_basic()
    print(df)
    print(type(df))
    df.to_csv(save_path)
    