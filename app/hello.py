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

# By default parameters are strings
@app.route('/greetings/<int:age>')
def greetings(age):
    return f'<h1>werffwerfwerd! {age}</h1>'

from markupsafe import escape

@app.route('code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
