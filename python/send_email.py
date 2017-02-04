#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'juxicn@163.com'
receiver = 'juxicn@gmail.com'
subject = 'Hi, this email send from 163.com, wish you a good holiday'

smtpserver = 'smtp.163.com'
username = 'juxicn@163.com'
password = 'justfor354'

msgRoot = MIMEMultipart('mixed')
msgRoot['Subject'] = 'test message'

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()


