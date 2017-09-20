from flask import Flask
my_app = Flask(__name__)

@my_app.route('/')
def root():
	return "//"
@my_app.route('/a')
def root():
	return "aa"
@my_app.route('/b')
def root():
	return "bb"

if __name__ == "__main__':
	my_app.run()
