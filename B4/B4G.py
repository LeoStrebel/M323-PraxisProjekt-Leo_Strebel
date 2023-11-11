from flask import Flask
from functools import reduce

app = Flask(__name__)

# Flask-Routen für die Anwendung von Map, Filter und Reduce
@app.route('/map_example')
def run_map_example():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Anwendung von Map mit Lambda-Ausdruck zur Verdopplung der Zahlen
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    return f'Doubled Numbers: {doubled_numbers}'

@app.route('/filter_example')
def run_filter_example():
    numbers = [1, 2, 3, 4, 5]
    # Anwendung von Filter mit Lambda-Ausdruck zur Auswahl gerader Zahlen
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return f'Even Numbers: {even_numbers}'

@app.route('/reduce_example')
def run_reduce_example():
    numbers = [1, 2, 3, 4, 5]
    # Anwendung von Reduce mit Lambda-Ausdruck zur Addition der Zahlen
    sum_numbers = reduce(lambda x, y: x + y, numbers)
    return f'Sum of Numbers: {sum_numbers}'

if __name__ == "__main__":
    app.run(debug=True)




