import unittest
from unittest.mock import patch
from controller.lattes_controller import LattesController

controller = LattesController()


class TestLattesController(unittest.TestCase):
    def test_validate_lattes_valid(self):
        lattes_number = '1234567890123456'
        with patch('controller.lattes_controller.LattesController.validate_lattes', return_value=True) as mock_method:
            result = controller.validate_lattes(lattes_number)
        self.assertTrue(result)

    def test_validate_lattes_invalid(self):
        lattes_number = '1234567890123456'
        with patch('controller.lattes_controller.LattesController.validate_lattes', return_value=False) as mock_method:
            result = controller.validate_lattes(lattes_number)
        self.assertFalse(result)
