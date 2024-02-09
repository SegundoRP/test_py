from flask import Flask

# represents flask app
app = Flask(__name__)

# represents principal route
@app.route('/')
def hello():
    return 'Hello world!'
