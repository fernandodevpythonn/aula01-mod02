from flask import render_template
from controllers.BaseController import BaseController

class HTMLbasicoController(BaseController):

    def __init__(self,app):
        self.rotas = [
            ('/','home', self.pagina_inicial)

        ]
        super().__init__(app)

    def pagina_inicial(self):
        return render_template("html_basico/basico.html")
