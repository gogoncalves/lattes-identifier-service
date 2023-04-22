from flask import Flask
from flasgger import Swagger
from controller.lattes_controller import LattesController
from service.lattes_service import LattesService
import os

app = Flask(__name__)
swagger = Swagger(app, template_file='swagger.yml')
controller = LattesController()
service = LattesService()


@app.before_first_request
def custom_startup_message():
    # If you leave this toggle in True it will perform web download
    if os.environ.get('ENABLE_LATTES_SEARCH', False):
        print(
            "Swagger UI: http://localhost:5000/apidocs\nEndpoint: http://localhost:5000/lattes/{lattes_number}\nParameter: lattes_number (Mandatory): Lattes identification number.")
        print("Starting Lattes Web Search Service...")
        # Change the URL address when you need to download the correct ZIPFILE
        url = "http://memoria.cnpq.br/documents/313759/83395da6-f582-46bc-a308-060a6ec1ceaa"
        destination_path = './' + 'static/'
        service.search_lattes_file(url, destination_path)
    else:
        print(
            "Swagger UI: http://localhost:5000/apidocs\nEndpoint: http://localhost:5000/lattes/{lattes_number}\nParameter: lattes_number (Mandatory): Lattes identification number.")


@app.route('/lattes/<int:lattes_number>')
def validate_lattes(lattes_number):
    return controller.validate_lattes(lattes_number)


if __name__ == '__main__':
    app.run()
