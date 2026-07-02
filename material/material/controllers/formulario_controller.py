from flask import render_template, request
from controllers.base_controller import BaseController

class FormularioController(BaseController):
    def __init__(self, app):
        self.rotas = [
            ('/formulario', 'formulario', self.proteger_rota(self.formulario)),
            ('/resultado', 'resultado', self.proteger_rota(self.resultado), ['POST']),
            ('/resultado_avancado', 'resultado_avancado', self.proteger_rota(self.resultado_avancado), ['POST']),
            ('/formulario_extra', 'formulario_extra', self.proteger_rota(self.formulario_extra)),
            ('/resultado_extra', 'resultado_extra', self.proteger_rota(self.resultado_extra), ['POST']),
        ]
        super().__init__(app)

    def formulario(self):
        return render_template("html_formularios/formulario.html")

    def resultado(self):
        nome = request.form['nome']
        email = request.form['email']
        return render_template("html_formularios/resultado.html", nome=nome, email=email)

    def resultado_avancado(self):
        nome = request.form.get('nome')
        email = request.form.get('email')
        nivel_conhecimento = request.form.get('nivel_conhecimento')
        hobbies = request.form.getlist('hobbies')

        if not nome or not email or not nivel_conhecimento or not hobbies:
            return "Por favor, preencha todos os campos obrigatórios!"

   
        mensagem = request.form.get('mensagem', '')
        curso = request.form.get('curso', '')
        return render_template("html_formularios/resultado.html",
                            nome=nome,
                            email=email,
                            mensagem=mensagem,
                            curso=curso,
                            nivel_conhecimento=nivel_conhecimento,
                            hobbies=hobbies)
    
    def formulario_extra(self):
        return render_template("html_formularios/formulario_extra.html")
    
    def resultado_extra(self):
        nome = request.form.get('nome')
        email = request.form.get('email')
        nascimento = request.form.get('nascimento')
        horario = request.form.get('horario')
        cor = request.form.get('cor')
        quantidade = request.form.get('quantidade')
        nota = request.form.get('nota')
        site = request.form.get('site')
        cidade = request.form.get('cidade')
        nivel_conhecimento = request.form.get('nivel_conhecimento')

       
        if not nome or not email or not nivel_conhecimento:
            return "Por favor, preencha os campos obrigatórios: nome, email e sexo."

       
        return render_template("resultado_avancado.html",
                               nome=nome,
                               email=email,
                               nascimento=nascimento,
                               horario=horario,
                               cor=cor,
                               quantidade=quantidade,
                               nota=nota,
                               site=site,
                               cidade=cidade,
                               nivel_conhecimento=nivel_conhecimento)