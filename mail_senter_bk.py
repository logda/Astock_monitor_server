#!/usr/bin/env python
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import datetime

def send_mail(gb_file_name_01, gb_file_name_02, config):
  sender = config['sender']['mail']
  password = config['sender']['password']

  #receivers = get_receiver("./config/receiver_mail")
  smtp_server = "smtp.qq.com"

  context = "每日涨停行业统计"
  message = MIMEMultipart()
  today_date = str(datetime.date.today())
  subject = "每日涨停行业统计"+today_date
  message['Subject'] = Header(subject)
  message['From'] = Header("蔡溢达")

  att1 = MIMEText(open('./data/'+gb_file_name_01 , 'rb').read(), 'base64', 'utf-8')
  att1["Content-Type"] = 'application/octet-stream'
  att1["Content-Disposition"] = 'attachment; filename="涨停行业统计.txt"'
  message.attach(att1)
  

  att2 = MIMEText(open('./data/'+gb_file_name_02 , 'rb').read(), 'base64', 'utf-8')
  att2["Content-Type"] = 'application/octet-stream'
  att2["Content-Disposition"] = 'attachment; filename="涨停行业成交量统计.txt"'
  message.attach(att2)

  server = smtplib.SMTP_SSL(smtp_server, 465)
  server.login(user=sender, password=password)

  server.sendmail(from_addr=sender, to_addrs=config['receivers'], msg=message.as_string())
  server.quit()
  print('邮件发送成功')






