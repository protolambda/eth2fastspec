build-dist:
	python3 setup.py sdist bdist_wheel

check-dist:
	python3 -m twine check dist/*

upload-dist:
	python3 -m twine upload dist/*

install:
	python3 -m venv venv && . venv/bin/activate; pip3 install .

clean:
	rm -rf build dist .pytest_cache *.egg-info
