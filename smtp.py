#!/usr/bin/python

import smtplib

sender = "marcusshepdotcom@gmail.com"
receiver = "sheph2mj@cmich.edu"

message = """From: A Guy <sheph2mj@cmich.edu>
To: Another Guy <sheph2mj@cmich.edu>
Subject: SMTP Email From Script
osjbdvojsbvojbd
This is an email sent from a python script."""

try:
	smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_obj.starttls()
	smtp_obj.login("marcusshepdotcom@gmail.com", "MJS33shep")
	smtp_obj.sendmail(sender, receiver, message)
	smtp_obj.quit()
	print "Auth was successful... Now sending email to: ", receiver

# print "Error: unable to send email."
