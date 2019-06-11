
all: debug

debug:
	export FLASK_APP=odd-one-out-basic.py ; export FLASK_ENV=development ; flask run

