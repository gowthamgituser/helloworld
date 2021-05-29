# packages for the program
from flask import Flask, request, session, render_template

app = Flask(__name__)


# API for hello-world
@app.route('/hello-world', methods=['GET'])
def index():
    return "HELLO WORLD"


# API to check palindrome
@app.route('/check-palindrome', methods=['POST'])
def palindrome():
    if request.method == 'POST':
        if 'view' in session:
            session['view'] = session.get('view') + 1
        else:
            session['view'] = 1
        return '''views count {}'''.format(session.get('view'))


# API to get session count
@app.route('/check-count', methods=['GET'])
def get_value():
    return "Total visit: {}".format(session.get('count'))

# Rerouting for invalid url request
@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'), 404

# Index
@app.route('/')
def check():
    return "CHECK RUN"


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'hello super key'
    app.run()
