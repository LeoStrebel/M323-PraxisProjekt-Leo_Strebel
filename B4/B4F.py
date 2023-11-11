from flask import Flask
from functools import reduce

app = Flask(__name__)


# Flask-Route für die kombinierte Anwendung von Map, Filter und Reduce
@app.route('/combined_example')
def run_combined_example():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Kombinierte Anwendung: Quadrieren, Filtern (gerade Zahlen) und Summieren
    result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))

    return f'Result of Combined Example: {result}'


if __name__ == "__main__":
    app.run(debug=True)


