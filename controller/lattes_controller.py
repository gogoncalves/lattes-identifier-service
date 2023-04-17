from flask import jsonify, make_response
from service.lattes_service import LattesService

LattesService = LattesService()


class LattesController:
    def __init__(self):
        pass

    def validate_lattes(self, lattes_number):
        is_valid = LattesService.validate_lattes(lattes_number)
        if is_valid:
            data = {
                'id_lattes': lattes_number,
                'message': 'Lattes validado com sucesso',
                'status': True
            }
            response = make_response(jsonify(data), 200)
            response.headers['Copyright'] = 'Copyright (c) 2023 Gustavo Goncalves.'
            return response
        else:
            data = {
                'id_lattes': lattes_number,
                'message': 'Numero de identificacao Lattes invalido',
                'status': False
            }
            response = make_response(jsonify(data), 404)
            response.headers['Copyright'] = 'Copyright (c) 2023 Gustavo Goncalves.'
            return response
