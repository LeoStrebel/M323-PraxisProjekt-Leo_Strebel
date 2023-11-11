from flask import Flask
app = Flask(__name__)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)


def swap(arr, i, j):
    """Vertauscht zwei Elemente in einer Liste."""
    arr[i], arr[j] = arr[j], arr[i]


# Flask-Route zum Aufrufen des Bubble Sort Algorithmus
@app.route('/bubble_sort')
def run_bubble_sort():
    my_list = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(my_list)
    return f'Sorted List (Bubble Sort): {my_list}'


if __name__ == "__main__":
    app.run(debug=True)
