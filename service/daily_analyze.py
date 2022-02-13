import pandas as pd

from common import path_util


def zhang_ting_analyze(date):  
  #__今日涨停的股票__
  daily_path = path_util.get_daily_path(date)
  df = pd.read_csv(daily_path)
  zhang_ting_df = df[(df["pct_chg"]>9.5) ]

  #__行业字典___
  industry_df = pd.read_csv(path_util.get_stock_basic_path())

  # # 数据预处理
  zhang_ting_df.loc['ts_code'] = zhang_ting_df['ts_code'].astype(str)
  industry_df['ts_code'] = industry_df['ts_code'].astype(str)
  temp = pd.merge(zhang_ting_df, industry_df, how="inner", on="ts_code")
  temp = temp[['ts_code', 'name', 'industry',"amount"]]
  temp['amount'] = temp[['amount']].apply(lambda x:x/100000000)
  
  # # 按照涨停股票个数排序
  hangye_count_gb = temp.groupby(['industry'])
  hangye_count_gb = (hangye_count_gb['amount'].agg(['count']).sort_values(by='count', ascending=False))

  # # 按照涨停股票成交量排序
  hangye_amt_gb = temp.groupby(['industry'])
  hangye_amt_gb = (hangye_amt_gb['amount'].agg(['sum']).sort_values(by='sum', ascending=False))
  return (hangye_count_gb, hangye_amt_gb)
