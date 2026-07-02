from flask import render_template, request, redirect, url_for, session
from controllers.base_controller import BaseController

class LoginController(BaseController):
    def __init__(self, app):
        self.rotas = [
            ('/login', 'login', self.login),
            ('/entrar', 'entrar', self.entrar, ['POST']),
            ('/logout', 'logout', self.logout),
        ]
        super().__init__(app)

        
        self.usuario_correto = "senac"  
        self.senha_correta = "12345"     

    def login(self):
        if session.get("usuario_logado"):
            return redirect(url_for("home"))  
        return render_template("html_login/login.html")

    def entrar(self):
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == self.usuario_correto and senha == self.senha_correta:
            session["usuario_logado"] = True
            return redirect(url_for("home"))
        else:
            erro = "Usuário ou senha incorretos!"
            return render_template("html_login/login.html", erro=erro)

    def logout(self):
        session.clear()
        return redirect(url_for("login"))