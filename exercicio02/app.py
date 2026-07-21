from controllers.html_basico_controller import htmlbasico
from flask import Flask

app = Flask(__name__)

htmlbasico(app)

if __name__ == "__main__":
    app.run(debug=True)