from flask import Flask
app = Flask(__name__)

# Flask-Route zum Aufrufen der Lambda-Ausdrücke
@app.route('/lambda_operations')
def run_lambda_operations():
    # Lambda-Ausdruck für das Quadrieren einer Zahl
    square = lambda x: x**2

    # Lambda-Ausdruck für das Konvertieren eines Strings in Großbuchstaben
    uppercase = lambda s: s.upper()

    # Anwendung der Lambda-Ausdrücke auf Werte
    result_square = square(5)
    result_uppercase = uppercase('hello')

    return f'Results: Square - {result_square}, Uppercase - {result_uppercase}'

if __name__ == "__main__":
    app.run(debug=True)


