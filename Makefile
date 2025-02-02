install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		python -m textblob.download_corpora

test:
	python3 -m pytest -vv --cov=corenlp test_corenlp.py
	

lint:
	pylint --disable=R,C *.py

format: 
	black *.py

all: install lint test format deploy