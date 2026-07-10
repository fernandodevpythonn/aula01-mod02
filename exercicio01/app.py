from flask import Flask
from controllers.html_basico_controller import HtmlBasico

app = Flask(__name__)
HtmlBasico(app)

if __name__ == "__main__":
    app.run(debug=True)