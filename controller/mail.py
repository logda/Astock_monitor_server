#!/usr/bin/env python
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import datetime

def send(path_1, path_2):
  sender = "yidacai@foxmail.com"
  password = ""

  #receivers = get_receiver("./config/receiver_mail")
  smtp_server = "smtp.qq.com"

  context = "每日涨停行业统计"
  message = MIMEMultipart()
  today_date = str(datetime.date.today())
  subject = "每日涨停行业统计"+today_date
  message['Subject'] = Header(subject)
  message['From'] = Header("蔡溢达")
  message['To'] = Header('subsciber')

  #__email main context__
  message.attach(MIMEText('此日期的涨停统计, 请注意查收附件！\n有问题随时沟通，谢谢！', 'plain', 'utf-8'))

  #__attachements__ 
  att1 = MIMEText(open(path_1 , 'rb').read(), 'base64', 'utf-8')
  att1["Content-Type"] = 'application/octet-stream'
  att1["Content-Disposition"] = 'attachment;filename="zt_industry_count.txt"'
  message.attach(att1)
  

  att2 = MIMEText(open(path_2 , 'rb').read(), 'base64', 'utf-8')
  att2["Content-Type"] = 'application/octet-stream'
  att2["Content-Disposition"] = 'attachment;filename="zt_volume_count.txt"'
  message.attach(att2)

  server = smtplib.SMTP_SSL(smtp_server, 465)
  server.login(user=sender, password=password)

  server.sendmail(from_addr=sender, to_addrs="yidacai@foxmail.com", msg=message.as_string())
  server.quit()
  print('邮件发送成功')






