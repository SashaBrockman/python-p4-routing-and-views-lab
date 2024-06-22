#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:something>')
def print_route(something):
    print(something)
    return something

@app.route('/count/<int:number>')
def count_route(number):
    counter = 0
    result = ''
    while(counter < number):
        print(counter)
        result += f'{counter}\n'
        counter += 1
    return result

@app.route('/math/<int:num1>/<string:opper>/<int:num2>')
def math_route(num1, opper, num2):
    result = 0
    if opper == '+':
        result = num1 + num2
    elif opper == '*':
        result = num1 * num2
    elif opper == "div":
        result = num1 / num2
    elif opper == "-":
        result = num1 - num2
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
