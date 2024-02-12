from flask import Flask, render_template

# represents flask app
app = Flask(__name__)

if __name__ == '__main__':
    app.run()

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

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'

@app.route('/example')
def example():
    numbers_list = [1, 2, 3, 4]
    return render_template('example.html', numbers_list = numbers_list)
