from flask import render_template#renderiza o modulo html
from controllers.base_controller import BaseController

class HTMLBasicoController(BaseController):

    def __init__(self,app):
        self.rotas = [#cria as rotas e adiciona em uma lista
            ('/', 'home', self.pagina_inicial),
            ('/perfil_profissional', 'perfil_profissional', self.pagina_perfil_profissional)
        ]
        super().__init__(app)

    def pagina_inicial(self):#definindo a pagina da pagina inicial
        return render_template("pagina_inicial.html")
    
    def pagina_perfil_profissional(self):#definindo a pagina do perfil profissional
        return render_template("perfil_profissional.html")