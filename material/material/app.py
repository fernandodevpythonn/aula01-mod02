from flask import Flask, session
from controllers.html_basico_controller import HTMLBasicoController
from controllers.formulario_controller import FormularioController
from controllers.login_controller import LoginController  

app = Flask(__name__)


app.secret_key = "senac"  

LoginController(app)
HTMLBasicoController(app)
FormularioController(app)

if __name__ == "__main__":
    app.run(debug=True)