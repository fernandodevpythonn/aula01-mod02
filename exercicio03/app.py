from flask import Flask
from controllers.html_base_controller import HTMLbasicoController
from controllers.formulario_controller import FormularioController
app = Flask(__name__)
HTMLbasicoController(app)
FormularioController(app)
if __name__ == "__main__":
    app.run(debug=True)