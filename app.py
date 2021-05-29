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
                    cnt = 0
                    indexes = []
                    for j in range(0, len(v1)):
                        flag = 1
                        # fact = len(v1)
                        data = v1[j].lower()
                        if data == "" or data == " ":
                            return '''Please check the value at {}'''.format(j)
                        # data = data.lower()
                        for i in range(0, int(len(data) / 2)):
                            if data[i] != data[len(data) - i - 1]:
                                flag = 0
                        if flag == 1:
                            cnt += 1
                            indexes.append(j)
                    if cnt == 0:
                        return '''No Palindromes found'''
                    else:
                        return '''{} Palindrome strings@indexes{}'''.format(cnt, indexes)
                else:
                    return '''Array cannot be empty'''


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
