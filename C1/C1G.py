from flask import Flask
app = Flask(__name__)

def calculate_sum(numbers):
    """Berechnet die Summe einer Liste von Zahlen."""
    return sum(numbers)

@app.route('/sum_example')
def sum_example():
    """Flask-Route für ein Beispiel mit Refactoring."""
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    return f'Die Summe der Zahlen ist: {result}'

if __name__ == "__main__":
    app.run(debug=True)


