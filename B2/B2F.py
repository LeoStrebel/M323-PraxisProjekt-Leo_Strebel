from flask import Flask
app = Flask(__name__)

def add(a, b):
    """Eine Funktion, die zwei Zahlen addiert."""
    return a + b

def multiply(a, b):
    """Eine Funktion, die zwei Zahlen multipliziert."""
    return a * b

def apply_operation(operation, x, y):
    """Eine Funktion, die eine Operation auf zwei Zahlen anwendet."""
    return operation(x, y)

# Flask-Route zum Aufrufen der Funktionen
@app.route('/calculate')
def run_calculate():
    num1, num2 = 5, 3
    result_addition = apply_operation(add, num1, num2)
    result_multiplication = apply_operation(multiply, num1, num2)
    return f'Results: Addition - {result_addition}, Multiplication - {result_multiplication}'

if __name__ == "__main__":
    app.run(debug=True)
