from flask import Flask

# represents flask app
app = Flask(__name__)

# represents principal route
@app.route('/')
@app.route('/index')
def index():
    return 'Inicio'

@app.route('/hello')
def hello():
    return '<h1>Hello world!</h1>'
