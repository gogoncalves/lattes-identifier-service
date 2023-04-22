from flask import jsonify, make_response
from service.lattes_service import LattesService

LattesService = LattesService()


class LattesController:
    def __init__(self):
        pass

    def validate_lattes(self, lattes_number):
        is_valid = LattesService.validate_lattes(lattes_number)
        data = {
            'idLattes': lattes_number,
            'status': is_valid,
            'message': 'Lattes successfully validated' if is_valid else 'Invalid Lattes identification number'
        }
        response = make_response(jsonify(data), 200 if is_valid else 404)
        response.headers['Copyright'] = 'Copyright (c) 2023 Gustavo Goncalves.'
        return response
