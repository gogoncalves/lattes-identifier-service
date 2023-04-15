from flask import Flask, request, jsonify
from flasgger import Swagger
from lattes_validator import LattesValidator

app = Flask(__name__)
swagger = Swagger(app)

validator = LattesValidator()

@app.route('/lattes/<int:lattes_number>', methods=['GET'])
def validate_lattes(lattes_number):
    """
    Este endpoint valida um número de identificação Lattes.

    ---
    parameters:
        - name: lattes_number
          in: path
          description: Número id Lattes
          type: integer
          required: true
    responses:
        200:
            description: Lattes validado com sucesso
        400:
            description: Número de identificação Lattes inválido
    """
    if validator.validate_lattes(lattes_number):
        return jsonify({"message": "Lattes validado com sucesso"}), 200
    else:
        return jsonify({"message": "Número de identificação Lattes inválido"}), 400

if __name__ == '__main__':
    app.run()