from controllers.html_basico_controller import HTMLbasicocontroller
from flask import Flask

app = Flask(__name__)

HTMLbasicocontroller(app)

if __name__ == "__main__":
    app.run(debug=True)