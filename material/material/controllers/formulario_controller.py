from flask import render_template, request
from controllers.base_controller import BaseController

class FormularioController(BaseController):
    def __init__(self, app):
        self.rotas = [
            ('/formulario', 'formulario', self.formulario),
            ('/resultado', 'resultado', self.resultado, ['POST']),
            ('/resultado_avancado', 'resultado_avancado', self.resultado_avancado, ['POST']),
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