import json
import re

from pygithub3 import Github
import gitlab

"""	
Short Script for iterating over issues in a gitlab project.
Then creating each issue in a specified repo on GitHub.
All values with '#' must be filled in by user.

requirements:
pyapi-gitlab==7.5.0
pygithub3==0.5.1
requests==2.5.3
"""

#gitlab
gl = gitlab.Gitlab("141.209.28.74", token="#", verify_ssl=False)

# github
auth = dict(login='#', password='#')
gh = Github(**auth)

project_ids = {
	'urec': 29,
	'centraldesk': 62,
	'sodium': 2,
}
issues = gl.getprojectissues(project_ids['urec'], per_page=100) # defaults to 20 results, max is 100
for i in range(len(issues)):
	""" 
	Currently pointing at urec, simply change 'urec' to any other
	value in project_ids in order to iterate over another project.
	"""
	
	date = gl.getprojectissues(project_ids['urec'])[i]['created_at']
	data = {
	'title': gl.getprojectissues(project_ids['urec'])[i]['title'],
	'body': "Date: "+ " ".join(re.split("T|\\.", date)[:2])+"\n"+" Desciption: "+gl.getprojectissues(project_ids['urec'])[i]['description'],

	}
	gh.issues.create(data, user='#', repo='#')
