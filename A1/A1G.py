from flask import Flask
app = Flask(__name__)

def add_numbers(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b


@app.route('/')
def home():
    """Flask-Route für die Startseite."""
    result = add_numbers(5, 7)
    return f'Das Ergebnis der Addition ist: {result}'


if __name__ == "__main__":
    app.run(debug=True)
