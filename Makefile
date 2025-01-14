install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		python -m textblob.download_corpora

test:
	#python3 -m pytest -vv --cov=grabImage test_grabImage.py
	#python -m pytest --nbval notebook.ipynb

lint:
	pylint --disable=R,C,E1120 nlpBlob.py

format: 
	black *.py

all: install lint test format deploy