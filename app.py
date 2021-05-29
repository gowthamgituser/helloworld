import sys

from flask import Flask, request, session, render_template

app = Flask(__name__)


@app.route('/hello-world', methods=['GET'])
def index():
    return "HELLO WORLD"


@app.route('/check-palindrome', methods=['POST'])
def palindrome():
    if request.method == 'POST':
        request_data = request.get_json()
        value = None
        if request_data:
            if 'value' in request_data:
                if (type(request_data['value']) == list) and (len(request_data['value']) > 0):
                    v1 = request_data['value']
                    data = v1[0]
                    if data == "":
                        return '''value is e'''
                    elif data == " ":
                        return '''value is empty'''
                    else:
                        return '''{}'''.format(data)


@app.route('/check-count', methods=['GET'])
def get_value():
    return "Total visit: {}".format(session.get('count'))


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'), 404


@app.route('/')
def check():
    return "CHECK RUN"


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super secret key'
    app.run()
