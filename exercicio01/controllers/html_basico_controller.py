from controllers.base_controller import BaseController
from flask import render_template

class HtmlBasico(BaseController):
    def __init__(self,app):
        self.rotas = [
            ('/positions','positions',self.pagina_positions),
            ('/','home',self.pagina_inicial)
        ]
        super().__init__(app)
    def pagina_positions(self):
        return render_template("positions.html")
    def pagina_inicial(self):
        return render_template("home.html")