import json
import re

from pygithub3 import Github
import gitlab

#gitlab
gl = gitlab.Gitlab("141.209.28.74", token="1isGAgVpjqresUDkwRNB", verify_ssl=False)

# github
auth = dict(login='#', password='#')
gh = Github(**auth)

project_ids = {
	'urec': 29,
	'centraldesk': 62,
	'sodium': 2,
}
issues = gl.getprojectissues(project_ids['urec'], per_page=100) # defaults to 20 results
for i in range(len(issues)):
	date = gl.getprojectissues(project_ids['urec'])[i]['created_at']

	data = {
	'title': gl.getprojectissues(project_ids['urec'])[i]['title'],
	'body': "Date: "+ " ".join(re.split("T|\\.", date)[:2])+"\n"+" Desciption: "+gl.getprojectissues(project_ids['urec'])[i]['description'],

	}
	gh.issues.create(data, user='#', repo='#')