nosetests -v --with-coverage --with-xunit ExperimentTest.py >result.txt 2>&1
python -m coverage xml --include=*