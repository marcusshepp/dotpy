#!/usr/bin/python
import sys
import os

_file = sys.argv[1]
vagrant = sys.argv[2]
cur_path = os.getcwd()
file_path = str(cur_path+"/"+_file)

os.chdir(vagrant)
os.system("vagrant halt")
os.system("vagrant up")
ready_file = "scp -P 2222 %s vagrant@localhost:/home/vagrant/" % file_path
os.system(ready_file)
os.system('vagrant ssh --command "dropdb vagrant"')
os.system('vagrant ssh --command "createdb vagrant"')
os.system('vagrant ssh --command "createuser user"')
os.system('vagrant ssh --command "pg_restore -d vagrant ~/%s"'% _file)
print "Done"
