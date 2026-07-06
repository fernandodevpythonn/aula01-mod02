from flask import render_template
from controllers.base_controller import BaseController

class HTMLBasicoController(BaseController):

    def __init__(self, app):
        self.rotas = [
            ('/', 'home', self.proteger_rota(self.pagina_inicial)),
            ('/estrutura', 'estrutura', self.proteger_rota(self.estrutura)),
            ('/titulos_textos', 'titulos_textos', self.proteger_rota(self.titulos_textos)),
            ('/links_imagens', 'links_imagens', self.proteger_rota(self.links_imagens)),
            ('/listas', 'listas', self.proteger_rota(self.listas)),
            ('/tabelas', 'tabelas', self.proteger_rota(self.tabelas)),
            ('/div', 'div', self.proteger_rota(self.div)),
            ('/semantica', 'semantica', self.proteger_rota(self.semantica)),
            ('/semantica_avancada', 'semantica_avancada', self.proteger_rota(self.semantica_avancada)),
            ('/midia', 'midia', self.proteger_rota(self.midia)),
        ]
        super().__init__(app)


    def pagina_inicial(self):
        return render_template("html_introducao/pagina_inicial.html")

    def estrutura(self):
        return render_template("html_introducao/estrutura_html.html")
    
    def titulos_textos(self):
        return render_template("html_introducao/titulos_textos.html")
    
    def links_imagens(self):
        return render_template("html_introducao/links_imagens.html")
    
    def listas(self):
        return render_template("html_introducao/listas.html")
    
    def tabelas(self):
        return render_template("html_introducao/tabelas.html")
    
    def div(self):
        return render_template("html_introducao/div.html")
    
    def semantica(self):
        return render_template("html_introducao/semantica.html")

    def semantica_avancada(self):
        return render_template("html_introducao/semantica_avancada.html")
    
    def midia(self):
        return render_template("html_introducao/midia.html")