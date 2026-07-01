from flask import render_template
from controllers.BaseController import BaseController

class HTMLbasicoController(BaseController):

    def __init__(self,app):
        self.rotas = [
            ('/formulario','formulario', self.pagina_formulario)

        ]
        super().__init__(app)

    def pagina_formulario(self):
        return render_template("formulario/formulario.html")
