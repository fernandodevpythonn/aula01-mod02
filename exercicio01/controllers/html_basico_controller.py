from flask import render_template
from controllers.base_controller import BaseController

class HTMLBasicoController(BaseController):

  def __init__(self,app):
    self.rotas = [
      ('/','links', self.pagina_links),
      ('/pagina_inicial','home',self.pagina_inicial)
    ]
    super().__init__(app)
  
  def pagina_links(self):
    return render_template("html_basico/pagina_links.html")
  def pagina_inicial(self):
    return render_template("html_basico/pagina_inicial.html")