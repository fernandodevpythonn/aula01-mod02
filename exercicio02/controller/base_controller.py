class BaseController:
    def __init__(self,app):
        self.app = app
        if hasattr(self,'rotas'):
            self.registrar_rotas()