from flask import Flask
app = Flask(__name__)

# Flask-Route zum Aufrufen von Lambda-Ausdrücken mit mehreren Argumenten
@app.route('/lambda_multiple_arguments')
def run_lambda_multiple_arguments():
    # Lambda-Ausdruck für die Addition von zwei Zahlen
    add_numbers = lambda x, y: x + y

    # Lambda-Ausdruck für die Konkatenation von zwei Strings
    concatenate_strings = lambda s1, s2: s1 + s2

    # Anwendung der Lambda-Ausdrücke auf Werte
    result_addition = add_numbers(3, 7)
    result_concatenation = concatenate_strings('Hello, ', 'World!')

    return f'Results: Addition - {result_addition}, Concatenation - {result_concatenation}'

if __name__ == "__main__":
    app.run(debug=True)

