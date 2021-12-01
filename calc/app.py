# Put your app in here.
'''Simple calculator APP with Flask, which uses URL query
parameters to get the numbers to calculate with.'''

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    '''Add a and b parameters'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def subtract():
    '''Subtract a and b parameters'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def multiply():
    '''Multiplies a and b parameters'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def divide():
    '''Divides a and b parameters'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)

##############################################################################
'''
Make a single route/view function that can deal with 4 different kinds of URLs:
/math/add
/math/sub
/math/mult
/math/div
Write this in one function with one route by using a route parameter 
for the actual operations
'''
operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<operator>')
def math(operator):
    '''Perform math operations on a and b parameters'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[operator](a, b)

    return str(result)
