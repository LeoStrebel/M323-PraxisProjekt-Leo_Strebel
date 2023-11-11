from flask import Flask
app = Flask(__name__)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        swap(arr, i, min_index)

def swap(arr, i, j):
    """Vertauscht zwei Elemente in einer Liste."""
    arr[i], arr[j] = arr[j], arr[i]


# Flask-Route zum Aufrufen des Selection Sort Algorithmus
@app.route('/selection_sort')
def run_selection_sort():
    my_list = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(my_list)
    return f'Sorted List (Selection Sort): {my_list}'


if __name__ == "__main__":
    app.run(debug=True)
