from flask import Flask
app = Flask(__name__)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Flask-Route zum Aufrufen des Bubble Sort Algorithmus
@app.route('/bubble_sort')
def run_bubble_sort():
    my_list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(my_list)
    return f'Sorted List (Bubble Sort): {my_list}'


if __name__ == "__main__":
    app.run(debug=True)
