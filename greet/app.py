from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    '''Returns the "welcome" text message on the page'''

    html = '<html><body><h1>welcome</h1></body></html>'
    return html

@app.route('/welcome/home')
def welcome_home():
    '''Returns the "welcome home" text message on the page'''

    html = '<html><body><h1>welcome home</h1></body></html>'
    return html

@app.route('/welcome/back')
def welcome_back():
    '''Returns the "welcome back" text message on the page'''

    html = '<html><body><h1>welcome back</h1></body></html>'
    return html

