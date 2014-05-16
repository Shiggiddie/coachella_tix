PYTHON = $(shell which python2.7)
ENV = $(CURDIR)/env

virtual-env:
	virtualenv --python=$(PYTHON) $(ENV)

env: virtual-env
	$(ENV)/bin/pip install -r requirements/base.txt

run: env
	$(ENV)/bin/python coachella.py

clean:
	rm -rf $(ENV)
