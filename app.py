from flask import Flask
from controllers.html_basico_controller import HtmlBasico_controller
from lista01.exercicio01.controllers.html_basico_controller01 import HTMLBasicoController01
from lista01.exercicio02.controllers.htmlbasico_controller02 import htmlbasicoController02
from lista01.exercicio03.controllers.htmlbasico_controller03 import htmlbasicoController03
from lista01.exercicio04.controllers.htmlbasico_controller04 import htmlbasicoController04
from lista01.exercicio05.controllers.htmlbasico_controller05 import htmlbasicoController05

from lista02.exercicio01.controllers.html_basico_controller0201 import HTMLBasicoController0201
from lista02.exercicio02.controllers.html_basico_controller0202 import HTMLBasicoController0202
from lista02.exercicio03.controllers.html_base_controller0203 import HTMLbasicoController0203
from lista02.exercicio03.controllers.formulario_controller import FormularioController

from lista03.exercicio01.controllers.html_basicocontroller0301 import htmlbasicocontroller0301
from lista03.exercicio01.controllers.logincontroller0301 import LoginController0301
from lista03.exercicio02.controllers.login_controller0302 import loginController0302
from lista03.exercicio02.controllers.html_basico_controller0302 import HTMLbasicocontroller0302
from lista03.exercicio03.controllers.html_basico_controller0303 import HTMLbasicoController0303
from lista03.exercicio03.controllers.login_controller0303 import login03Controller0303
from lista03.exercicio04.controllers.login_controller0304 import LoginController0304
from lista03.exercicio04.controllers.htmlbasico_controller0304 import HTMLbasicoController0304
app = Flask(__name__)
HtmlBasico_controller(app)



HTMLBasicoController01(app)
htmlbasicoController02(app)
htmlbasicoController03(app)
htmlbasicoController04(app)
htmlbasicoController05(app)


HTMLBasicoController0201(app)
HTMLBasicoController0202(app)
HTMLbasicoController0203(app)
FormularioController(app)

htmlbasicocontroller0301(app)
LoginController0301(app)
app.secret_key = "log_ex01"

HTMLbasicocontroller0302(app)
loginController0302(app)
app.secret_key = "log_ex02"

HTMLbasicoController0303(app)
login03Controller0303(app)
app.secret_key = "log_ex03"

HTMLbasicoController0304(app)
LoginController0304(app)

if __name__ == "__main__":
  app.run(debug=True)