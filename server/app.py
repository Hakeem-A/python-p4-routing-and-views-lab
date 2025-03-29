#!/usr/bin/env python3

from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count_route(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<num1>/<op>/<num2>')
def math_route(num1, op, num2):
    num1 = float(num1)
    num2 = float(num2)
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div':
        return f"{num1 / num2:.1f}"
    elif op == '%':
        result = num1 % num2
    
    return str(int(result) if result.is_integer() else result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
