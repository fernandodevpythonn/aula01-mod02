from flask import Flask

from controllers.htmlbasico_controller import htmlbasicoController

app = Flask(__name__)

htmlbasicoController(app)

if __name__ == "__main__":
    app.run(debug=True)