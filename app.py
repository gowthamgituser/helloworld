from flask import Flask

apps = Flask(__name__)
@app.route('/')
def check():
    return "CHECK RUN"


if __name__ == '__main__':
    apps.run()