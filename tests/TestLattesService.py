import unittest
from unittest.mock import patch
from service.lattes_service import LattesService

service = LattesService()

class TestLattesService(unittest.TestCase):
    def test_validate_lattes_valid(self):
        lattes_number = '1234567890123456'
        with patch('service.lattes_service.LattesService.search_lattes_in_mysql', return_value=True) as mock_method:
            result = service.validate_lattes(lattes_number)
        self.assertTrue(result)
        
    def test_validate_lattes_valid_double(self):
        lattes_number = '1234567890123456'
        with patch('service.lattes_service.LattesService.search_lattes_in_mysql', return_value=False) as mock_method:
            with patch('service.lattes_service.LattesService.search_lattes_in_csv', return_value=True) as mock_method2:
                result = service.validate_lattes(lattes_number)
        self.assertTrue(result)

    def test_validate_lattes_invalid_double_true(self):
        lattes_number = '1234567890123456'
        with patch('service.lattes_service.LattesService.search_lattes_in_mysql', return_value=True) as mock_method:
            with patch('service.lattes_service.LattesService.search_lattes_in_csv', return_value=True) as mock_method2:
                result = service.validate_lattes(lattes_number)
        self.assertTrue(result)

    def test_validate_lattes_invalid_double_false(self):
        lattes_number = '1234567890123456'
        with patch('service.lattes_service.LattesService.search_lattes_in_mysql', return_value=False) as mock_method:
            with patch('service.lattes_service.LattesService.search_lattes_in_csv', return_value=False) as mock_method2:
                result = service.validate_lattes(lattes_number)
        self.assertFalse(result)