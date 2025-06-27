#!/usr/bin/env python3

import smtplib, ssl
import os 
from email.message import EmailMessage 

email_sender = 'captaintn3612@gmail.com'
email_password = "thomas2002"

email_receiver = 'thomas.nguyen3612@gmail.com'

subject = "Hello"

body = """
My name is Thomas
"""

em = EmailMessage()
em['From'] = email_sender 
em['To'] = email_receiver 
em['Subject'] = subject 
em.set_content(body) 

context = ssl.create_default_context() 

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
    smtp.login(email_sender, email_password) 
    smtp.sendmail(email_sender, email_receiver, em.as_string()) 
    