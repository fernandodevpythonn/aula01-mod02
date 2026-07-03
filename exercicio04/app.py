from flask import Flask
from controllers.htmlbasico_controller import HTMLbasicoController
app = Flask(__name__)
HTMLbasicoController(app)
if __name__ == "__main__":
    app.run(debug=True)