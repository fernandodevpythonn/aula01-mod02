from flask import render_template, request, redirect, url_for, session
from controllers.base_controller import BaseController

class LoginController(BaseController):
    def __init__(self, app):
        self.rotas = [
            ('/login', 'login', self.login),
            ('/entrar', 'entrar', self.entrar, ['POST']),
            ('/cadastro', 'cadastro', self.cadastro),
            ('/registrar', 'registrar', self.registrar, ['POST']),
            ('/logout', 'logout', self.logout),
        ]
        super().__init__(app)

        self.usuarios =[{"usuario":"senac","senha": "12345"}]
        # self.usuario_correto = "senac"  
        # self.senha_correta = "12345"     

    def login(self):
        if session.get("usuario_logado"):
            return redirect(url_for("home"))  
        return render_template("html_login/login.html")

    def entrar(self):
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        usuario_valido = next((u for u in self.usuarios if u["usuario"] == usuario and u["senha"] == senha), None)
        if usuario_valido:
            session["usuario_logado"]=True
            return redirect(url_for("home"))
        else:
            erro = "Usuario ou senha incorretos!"
            return render_template("html_login/login.html")


        # if usuario == self.usuario_correto and senha == self.senha_correta:
        #     session["usuario_logado"] = True
        #     return redirect(url_for("home"))
        # else:
        #     erro = "Usuário ou senha incorretos!"
        #     return render_template("html_login/login.html", erro=erro)

    def logout(self):
        session.clear()
        return redirect(url_for("login"))
    
    def cadastro(self):
       return render_template("html_login/cadastro.html")
    

    def registrar(self):
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        email = request.form.get("email")
        nascimento = request.form.get("nascimento")

        if not usuario or not senha or not email or not nascimento:
            erro = "Todos os campos são obrigatórios!"
            return render_template("html_login/cadastro.html", erro=erro)

        self.usuarios.append({
            "usuario": usuario,
            "senha": senha,
            "email": email,
            "nascimento": nascimento
        })

        sucesso = "Cadastro realizado! Faça login."
        return render_template("html_login/login.html", sucesso=sucesso)