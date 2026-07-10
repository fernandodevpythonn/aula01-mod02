from controllers.base_controller import BaseController
from flask import render_template

class HtmlBasico(BaseController):
    def __init__(self,app):
        self.rotas = [
            ('/','home',self.pagina_home)
        ]
        super().__init__(app)
    def pagina_home(self):
        return render_template("home.html")