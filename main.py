from flask import Flask
from flasgger import Swagger
from controller.lattes_controller import LattesController

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yml')

controller = LattesController()


@app.before_first_request
def custom_startup_message():
    print("Swagger UI: http://localhost:5000/apidocs")
    print("Endpoint: http://localhost:5000/lattes/{lattes_number}")
    print("Parâmetro: lattes_number (obrigatório): Número de identificação Lattes.")


@app.route('/lattes/<int:lattes_number>', methods=['GET'])
def validate_lattes(lattes_number):
    return controller.validate_lattes(lattes_number)


if __name__ == '__main__':
    app.run()
