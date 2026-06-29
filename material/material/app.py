
from flask import Flask
from controllers.html_basico_controller import HTMLBasicoController
from controllers.formulario_controller import FormularioController
app = Flask(__name__)

HTMLBasicoController(app)
FormularioController(app)

if __name__ == "__main__":
    app.run(debug=True)