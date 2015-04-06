#!/usr/bin/python
import sys
import smtplib

import praw

r = praw.Reddit(user_agent="AqmUmhPnyeHsVd_N1rIJTYmxyhY")
sender = "marcusshepdotcom@gmail.com"
receiver = "2487985570@vtext.com"
subject = str(sys.argv[1])
reddit_posts = r.get_subreddit(str(sys.argv[1])).get_hot(limit=3)
posts = [str(x) for x in reddit_posts]

message = """From: A Guy <sheph2mj@cmich.edu>
To: Johnathan <machine@techops.edu>
Subject: %s \n

\n
%s
\n
%s
\n
%s
""" % (subject, posts[0], posts[1], posts[2])

try:
	print "Searching reddit for:", subject
	smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_obj.starttls()
	smtp_obj.login("marcusshepdotcom@gmail.com", "MJS33shep")
	smtp_obj.sendmail(sender, receiver, message)
	print "Auth was successful... Now sending email to: ", receiver
finally:
	smtp_obj.quit()

# print "Error: unable to send email."
