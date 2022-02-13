

def get_daily_path(date):
    return './data/daily/' + str(date.strftime("%Y%m%d")) + '/daily.csv'

def get_stock_basic_path():
    return "./data/stock_basic.csv"