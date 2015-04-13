#!/usr/bin/python
import sys

import praw

def read_reddit(subreddit):

	""" Initialize Reddit """
	r = praw.Reddit(user_agent="AqmUmhPnyeHsVd_N1rIJTYmxyhY")
	submissions = r.get_subreddit(subreddit).get_top(limit=5)
	
	""" Retrieve Posts """
	# posts = [str(x) for x in submissions]

	""" Retrieve Comments """
	sub = next(submissions) # THIS IS BROKEN GG
	comments = []
	for key in xrange(5):
		try:
			comments.append(str(sub.comments[key].body))
		except:
			print "Not enough posts to populate list"
	
	""" Create Message """
	message = """
	Subreddit: %s \n
	%s
	\n
	%s
	\n
	%s
	\n
	%s
	\n
	%s
	""" % (subreddit, str(sub.title), comments[0], comments[1], comments[3], comments[4])

	return message

if __name__ == "__main__":
	arg = str(sys.argv[1])
	print read_reddit(arg)