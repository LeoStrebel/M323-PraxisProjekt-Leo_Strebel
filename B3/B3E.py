from flask import Flask
app = Flask(__name__)


# Flask-Route zum Sortieren von Wörtern mit Lambda-Ausdruck
@app.route('/lambda_sort')
def run_lambda_sort():
    words = ['Apple', 'Banana', 'Orange', 'Grapes', 'Cherry']

    # Lambda-Ausdruck zur Sortierung nach Wortlänge
    sorted_words = sorted(words, key=lambda x: len(x))

    return f'Sorted Words: {sorted_words}'


if __name__ == "__main__":
    app.run(debug=True)


