#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display C followed
    along with the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Display Python
    along with the text variable
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n is a number
    only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display HTML page with odd or even integer
    States whether <n> is even or odd
    """
    #checks if n is an interger
    if isinstance(n, int):
        #determine if n is even or odd
        even_or_odd = "even" if n % 2 == 0 else "odd"
        #Render the template and pass the
        #value of n and even_or _odd to the template
    return render_template('6-number_odd_or_even.html', n=n, even_or_odd=even_or_odd)
else:
    #if n is not an integer, return an error message
    return "Invalid input. Please provide an integer."



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
