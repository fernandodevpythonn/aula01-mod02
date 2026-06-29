from flask import render_template
from controllers.base_controller import BaseController

class HTMLBasicoController(BaseController):

    def __init__(self, app):
        self.rotas = [
            ('/', 'home', self.pagina_inicial),
            ('/estrutura', 'estrutura', self.estrutura),
            ('/titulos_textos', 'titulos_textos', self.titulos_textos),
            ('/semantica', 'semantica', self.semantica),
            ('/links_imagens', 'links_imagens', self.links_imagens),
        ]
        super().__init__(app)

   
    def pagina_inicial(self):
        return render_template("html_introducao/pagina_inicial.html")

    def estrutura(self):
        return render_template("html_introducao/estrutura_html.html")
    
    def titulos_textos(self):
        return render_template("html_introducao/titulos_textos.html")
    
    def semantica(self):
        return render_template("html_introducao/semantica.html")
    
    def links_imagens(self):
        return render_template("html_introducao/links_imagens.html")