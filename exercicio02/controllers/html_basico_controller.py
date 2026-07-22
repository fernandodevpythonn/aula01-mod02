from controllers.base_controller import BaseController
from flask import render_template
class htmlbasico(BaseController):
    def __init__(self,app):
        self.rotas = [
            ('/','home',self.pagina_inicial),
            ('/cards','cards',self.pagina_cards)
        ]
        super().__init__(app)

    def pagina_inicial(self):
        return render_template("pagina_inicial.html")
    def pagina_cards(self):
        return render_template("cards.html")