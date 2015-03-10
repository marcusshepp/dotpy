import json
from pygithub3 import Github
import gitlab


#gitlab
gl = gitlab.Gitlab("141.209.28.74", token="1isGAgVpjqresUDkwRNB", verify_ssl=False)

# github
auth = dict(login='marcusshepp', password='MJS33shep')
gh = Github(**auth)
data = {"title": "TEST"}

# 
# print json.dumps(, sort_keys=True, indent=4, separators=(",", ": "))
projects = gl.getprojects() # defaults to 20 results
for i in range(len(projects)):
	print gl.getprojectissues(projects[i]['id']) # defaults to 20 results
	# gh.issues.create(data, user='marcusshepp', repo='dotpy')


