##########################################################################
### Dependancies
##########################################################################

install-apt:
	xargs apt-get -y install < apt-requirements.txt

install: install-apt
	pip3 install --user -r requirements-lock.txt

install-dev:
	pip3 install --user -r requirements.txt

##########################################################################
### Building
##########################################################################

build:
	pass

freeze-requirements:
	pip3 freeze > requirements-lock.txt

##########################################################################
### Development
##########################################################################

workspace:
	python 3 -m venv .venv
	${make} install-dev

##########################################################################
### Runtime
##########################################################################

start:
	gunicorn --chdir ./src main:app --reload