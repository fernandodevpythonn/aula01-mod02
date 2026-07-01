from flask import render_template
from controllers.base_controller import BaseController

class HTMLBasicoController(BaseController):
    def __init__(self,app):
     self.rotas = [
        ('/','imagens',self.pagina_imagens),
        ('/pagina_inicial','home',self.pagina_inicial)
     ]
     super().__init__(app)

    def pagina_imagens(self):
       return render_template("pagina_imagens.html")
    def pagina_inicial(self):
       return render_template("pagina_inicial.html")