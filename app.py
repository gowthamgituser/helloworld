from flask import Flask

app = Flask(__name__)

@app.route('/hello-world', methods=['GET'])
def index():
    return "HELLO WORLD"


@app.route('/')
def check():
    return "CHECK RUN"


if __name__ == '__main__':
    app.run()