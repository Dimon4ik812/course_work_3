import unittest
from unittest import mock
from unittest.mock import patch
import json
from src.api_hh import GetInfoHHCompany

class TestGetInfoHHCompany(unittest.TestCase):
    def setUp(self):
        self.hh_company = GetInfoHHCompany()

    @patch('requests.get')
    def test_get_employer_info(self, mock_get):
        # Arrange
        employer_id = 1234
        mock_response = {
            "id": "1234",
            "name": "Acme Inc.",
            "description": "Acme is a leading company in the industry."
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Act
        result = self.hh_company.get_employer_info(employer_id)

        # Assert
        self.assertEqual(result, mock_response)
        mock_get.assert_called_once_with(f"{self.hh_company.base_url}/employers/{employer_id}", headers=self.hh_company.headers)


if __name__ == '__main__':
    unittest.main()