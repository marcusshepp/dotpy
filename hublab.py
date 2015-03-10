import json
from pygithub3 import Github
import gitlab

#gitlab
gl = gitlab.Gitlab("141.209.28.74", token="1isGAgVpjqresUDkwRNB", verify_ssl=False)

# github
auth = dict(login='marcusshepp', password='MJS33shep')
gh = Github(**auth)

project_ids = {
	'urec': 29,
	'centraldesk': 62,
	'sodium': 2,
}
urec = project_ids['urec']


projects = gl.getprojects(per_page=100) # defaults to 20 results
# for i in range(len(projects)):
 	# print "-----"
 	# print projects[i]['id']
 	# print gl.getproject(projects[i]['id'])['http_url_to_repo']
	
issues = gl.getprojectissues(urec, per_page=100) # defaults to 20 results
for i in range(len(issues)):

	data = {
	'title': gl.getprojectissues(urec)[i]['title'],
	'body': gl.getprojectissues(urec)[i]['description'],
	}
	gh.issues.create(data, user='marcusshepp', repo='cmu-techops/sodium')
	
result = gh.repos.list_by_org('cmu-techops')
for resource in result.iterator():
	print resource