from flask import Flask
app = Flask(__name__)

def greet(name):
    """Eine Funktion, die eine Begrüßung zurückgibt."""
    return f'Hello, {name}!'

# Funktion als Objekt speichern
test_function = greet

# Funktion in einer Variable weitergeben
def execute_function(func, parameter):
    return func(parameter)

# Flask-Route zum Aufrufen der Funktion
@app.route('/execute_greet')
def run_execute_greet():
    name = 'John'
    result = execute_function(test_function, name)
    return f'Result: {result}'

if __name__ == "__main__":
    app.run(debug=True)
