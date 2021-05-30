# packages for the program
from flask import Flask, request, session, render_template
from multiprocessing import Value

counter = Value('i', 0)
# Flask app name
app = Flask(__name__)
visit = 0


# To Check API for hello-world
@app.route('/hello-world', methods=['GET'])
def index():
    return "HELLO WORLD"


# To Check API for check palindrome
@app.route('/check-palindrome', methods=['POST'])
def palindrome():
    if request.method == 'POST':
        with counter.get.lock():
            counter.value += 1

        """if 'count' in session:
            session['count'] = session.get('count') + 1
        else:
            session['count'] = 1"""
        global visit
        visit += 1
        request_data = request.get_json()
        value = None
        if request_data:
            if 'value' in request_data:
                if (type(request_data['value']) == list) and (len(request_data['value']) > 0):
                    v1 = request_data['value']
                    v1 = [x.strip() for x in v1]
                    v1 = [x.rstrip() for x in v1]
                    cnt = 0
                    indexes = []
                    for j in range(0, len(v1)):
                        flag = 1
                        # fact = len(v1)
                        data = v1[j].lower()
                        if data == "":
                            return '''Please check the value at index level'''
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


"""
@app.route('/check-palindrome')
def palindrome():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    return '''  '''
"""


# API to get session count
@app.route('/check-count', methods=['GET'])
def get_value():
    # return "Total visit: {}".format(session.get('count'))
    return "Total visit: {}".format(counter.value)


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
    app.secret_key = 'hell0 super key'
    app.run()
