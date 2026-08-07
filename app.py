from flask import Flask
from controllers.html_basico_controller import HtmlBasico_controller
app = Flask(__name__)
HtmlBasico_controller(app)

if __name__ == "__main__":
  app.run(debug=True)