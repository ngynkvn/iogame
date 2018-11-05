from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return app.send_static_file('index.html')

@app.route('/api/<user>')
def user(user=None):
    return 'HI: ' + user