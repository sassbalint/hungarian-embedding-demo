
all: debug

debug:
	export FLASK_APP=ooo_flask.py ; export FLASK_ENV=development ; flask run

