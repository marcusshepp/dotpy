from invoke import task, run

@task
def vm():
	run("pip uninstall virtualenv")
	run("pip uninstall virtualenvwrapper")
	run("vim ~/.profile")
	run(":q")