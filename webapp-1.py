from flask import Flask

app = Flask(__name__)


@app.route('/')
def ciao():
    return '<h1>Ciao!</h1>'
