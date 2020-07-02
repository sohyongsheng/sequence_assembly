# Need to remove pkg-resources==0.0.0, 
# as it is a bug with Debian.
# See following site for more details:
# https://stackoverflow.com/questions/39577984/what-is-pkg-resources-0-0-0-in-output-of-pip-freeze-command
.PHONY: requirements
requirements:
	pip3 freeze | sed '/pkg-resources/d' > requirements.txt
