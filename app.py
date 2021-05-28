from flask import Flask, render_template, request, session
from urllib.request import urlopen
import json

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
                    #return ''' value is: {}'''.format(v1)
                    for j in range(0, len(v1)):
                        fact = len(v1)
                        data = v1[j]
                        for i in range(0, int(len(data)/2)):
                            if data[i] != data[len(data) -i - 1]:
                                return "Not a palindrome"
                        return '''palindrome: {}'''.format(data)
                else:
                    return '''Array cannot be empty'''
            #if v1 == []:
            #return '''Array Cannot be empty'''
        #else:
            #return ''' vallues {}.'''.format(v1[3])
        #for i in range(0, int(len(value) / 2)):
            #if value[i] != value[len(value) - i - 1]:
                #return "Not a palindrome"
        #return '''palindrome: {}'''.format(value)

@app.route('/')
def check():
    return "CHECK RUN"


if __name__ == '__main__':
    app.debug=True
    app.secret_key = 'super secret key'
    app.run()