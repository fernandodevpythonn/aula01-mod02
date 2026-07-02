from functools import wraps
from flask import render_template, request, redirect,url_for,session
from controllers.basecontroller import BaseController

class LoginController(BaseController):
    def __init__(self,app):
        self.rotas = [
            ('/formulario','formulario',self.pagina_login)
        ]
        super().__init__(app)
        self.usuario_correto = "fernando"
        self.email_correto = "fernando@123"

    def pagina_login(self):
        return render_template("login/pagina_login.html")
    
    def resultados(self):
        nome = request.form.get('nome')
        email = request.form.get('email')

        if not nome or not email:
            return "por favor, preencha os campos"
        
        return render_template("login/pagina_login.html",
                nome = nome,
                email = email)
    def login(self):
        if session.get("usuario_logado"):
            return redirect(url_for("home"))
        return render_template("basico_html/pagina_inicial.html")
        
    def entrar(self):
        usuario = request.form.get("nome")
        email = request.form.get("email")

        if usuario == self.usuario_correto and email == self.email_correto:
            session["usuario_logado"] = True
            return redirect(url_for("home"))
        return render_template("basico_html/pagina_inicial.html")