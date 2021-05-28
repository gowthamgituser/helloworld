from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/hello-world', methods=['GET'])
def index():
    return "HELLO WORLD"

@app.route('/check-palindrome', methods=['POST'])
def palindrome():
    if request.method == 'POST':
        value = request.args.get('value')
        for i in range(0, int(len(value) / 2)):
            if value[i] != value[len(value) - i - 1]:
                return "Not a palindrome"
        return '''palindrome: {}'''.format(value)

@app.route('/')
def check():
    return "CHECK RUN"


if __name__ == '__main__':
    app.debug=True
    app.secret_key = 'super secret key'
    app.run()