from flask import Flask
app = Flask(__name__)

def outer_function(prefix):
    """Eine äußere Funktion, die ein Präfix akzeptiert."""
    def inner_function(name):
        """Eine innere Funktion, die das Präfix auf den Namen anwendet."""
        return f'{prefix} {name}'
    return inner_function

# Flask-Route zum Aufrufen der Funktionen mit Closures
@app.route('/greet_with_closure')
def run_greet_with_closure():
    greet_with_hello = outer_function('Hello,')
    greet_with_hi = outer_function('Hi,')

    result1 = greet_with_hello('John')
    result2 = greet_with_hi('Alice')

    return f'Results: {result1}, {result2}'

if __name__ == "__main__":
    app.run(debug=True)


