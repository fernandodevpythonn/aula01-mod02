from flask import Flask
from controllers.html_basico_controller import HtmlBasico_controller
from lista01.exercicio01.controllers.html_basico_controller01 import HTMLBasicoController01
app = Flask(__name__)
HtmlBasico_controller(app)
HTMLBasicoController01(app)
if __name__ == "__main__":
  app.run(debug=True)