#!/usr/bin/python

import smtplib

sender = "sheph2mj@cmich.edu"
receiver = "2487985570@vtext.com"

message = """From: A Guy <sheph2mj@cmich.edu>
To: Another Guy <sheph2mj@cmich.edu>
Subject: SMTP Email From Script
osjbdvojsbvojbd
This is an email sent from a python script."""


smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.starttls()
smtp_obj.login("marcusshepdotcom@gmail.com", "#")
smtp_obj.sendmail(sender, receiver, message)
smtp_obj.quit()
print "Auth was successful... Now sending email to: ", receiver

# print "Error: unable to send email."
