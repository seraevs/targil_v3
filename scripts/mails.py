#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_mail(filename_report,
              mail_subject,
              mail_from,
              mail_to,
              mail_cc,              
              html,
              files,
              dir_path,
              ip_smtp,
              port_smtp):
    print("===== Test 1 =====")
    msg = MIMEMultipart("alternative")
    msg["Subject"] = mail_subject
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg["Cc"] = mail_cc
    part = MIMEText(html, "html")
    msg.attach(part)
    if dir_path != "":
        with open(filename_report, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        for f in files:  # add files to the message
            file_path = os.path.join(dir_path, f)
            attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename=f)
            msg.attach(attachment)

    server = smtplib.SMTP(ip_smtp, port_smtp)
    mail_list = [mail_to, mail_to]
    amount = []
    name = ['Sergey']
    server.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
    print("===== Test 2 =====")
