from flask import Flask, request, jsonify, make_response
from flasgger import Swagger
from domain.lattes_validator import LattesValidator

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yml')

validator = LattesValidator()


@app.before_first_request
def custom_startup_message():
    print("Swagger UI: http://localhost:5000/apidocs")
    print("Endpoint: http://localhost:5000/lattes/{lattes_number}")
    print("Parâmetro: lattes_number (obrigatório): Número de identificação Lattes.")


@app.route('/lattes/<int:lattes_number>', methods=['GET'])
def validate_lattes(lattes_number):
    if validator.validate_lattes(lattes_number):
        data = {
            'id_lattes': lattes_number,
            'message': 'Lattes validado com sucesso',
            'status': True
        }
        response = make_response(jsonify(data), 200)
        response.headers['Copyright'] = 'Copyright (c) 2023 Gustavo Goncalves. All rights reserved.'
        return response
    else:
        data = {
            'id_lattes': lattes_number,
            'message': 'Numero de identificacao Lattes invalido',
            'status': False
        }
        response = make_response(jsonify(data), 404)
        response.headers['Copyright'] = 'Copyright (c) 2023 Gustavo Goncalves. All rights reserved.'
        return response


if __name__ == '__main__':
    app.run()
