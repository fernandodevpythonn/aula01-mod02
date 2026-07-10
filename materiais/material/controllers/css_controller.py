from flask import render_template
from controllers.base_controller import BaseController

class CSScontroller(BaseController):
    def __init__(self, app):
        self.rotas=[
        ('/seletores','seletores',self.proteger_rota(self.seletores)),
        ('/modelo_caixa', 'modelo_caixa', self.proteger_rota(self.modelo_caixa)),
        ('/estilos_texto', 'estilos_texto', self.proteger_rota(self.estilos_texto)),
        ]
        super().__init__(app)


    def seletores(self):
        return render_template("css_introducao/seletores.html")

    def modelo_caixa(self):
        return render_template ("css_introducao/modelo_caixa.html")
    
    def estilos_texto(self):
        return render_template("css_introducao/estilos_texto.html")