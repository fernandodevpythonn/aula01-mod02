from controllers.base_controller import BaseController
from flask import render_template
class HtmlBasico_controller(BaseController):
  def __init__(self,app):
    self.rotas = [
      ('/','home',self.pagina_incial)
    ]
    super().__init__(app)

  def pagina_incial(self):
    return render_template("basico/home.html")