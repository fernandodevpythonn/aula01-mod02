class BaseController:
    """
    faz analize das rotas
    """
    def __init__(self, app):
        self.app = app
        if hasattr(self,'rotas'):#verifica se existe o atributo rotas
            self.registrar_rotas()#se existe o atributo rota, ele registra a rota
    def registrar_rotas(self):
        for rota in self.rotas:
            endereco_url, nome_rota, funcao_resposta = rota#rota recebe o endereco url, nome da rota e a funcao da rota
            self.app.add_url_rule(endereco_url, nome_rota,funcao_resposta)