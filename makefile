upload:
	python setup.py sdist upload -r pypi
check:
	python setup.py check -r -s