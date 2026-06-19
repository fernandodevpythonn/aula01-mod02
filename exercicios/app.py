from flask import Flask
from controllers.html_basico_controller import HTMLBasicoController

app = Flask(__name__)

HTMLBasicoController(app)

if __name__ == "__main__":
    app.run(debug=True)