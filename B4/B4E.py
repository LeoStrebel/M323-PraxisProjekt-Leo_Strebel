from flask import Flask
from functools import reduce

app = Flask(__name__)


# Flask-Route für eine komplexe Datenverarbeitungsaufgabe
@app.route('/complex_processing')
def complex_processing():
    data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 15},
        {'id': 3, 'value': 8},
        {'id': 4, 'value': 12}
    ]

    # Anwendung von Map, Filter und Reduce auf Datenstrukturen
    result = reduce(lambda acc, item: acc + item['value'], filter(lambda x: x['value'] > 10, data), 0)

    return f'Result of Complex Processing: {result}'


if __name__ == "__main__":
    app.run(debug=True)


