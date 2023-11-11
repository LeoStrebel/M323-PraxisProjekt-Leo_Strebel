from flask import Flask
app = Flask(__name__)


def modify_string(original):
    """Modifiziert den übergebenen String und gibt eine Kopie zurück."""
    modified = original.upper()  # Beispiel für eine unveränderliche Operation
    return f"Modifizierter String: {modified}"


@app.route('/')
def home():
    """Flask-Route für die Startseite."""
    original_string = "Hallo, Welt!"
    result = modify_string(original_string)
    return result


if __name__ == "__main__":
    app.run(debug=True)
