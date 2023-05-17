import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from app import app
from src.rest.controllers import Controllers


class TestRest(unittest.TestCase):
    def setUp(self):
        self.controllers = Controllers()
        self.tester = app.test_client(self)

    @patch("src.rest.controllers.Controllers")
    def test_health_route(self, mock_controllers: MagicMock) -> None:
        """Test should call controllers health route method once"""
        controllers = mock_controllers.return_value
        controllers.health_route().return_value = MagicMock()
        
        response = self.tester.get('/health')
        controllers.health_route.assert_called_once()
    
    @patch("src.rest.controllers.Controllers")
    def test_pokemon_list(self, mock_controllers: MagicMock) -> None:
        """Test should call controllers pokemon list method once"""
        controllers = mock_controllers.return_value
        controllers.pokemon_list().return_value = MagicMock()
        response = self.tester.get('/pokemon/list')
        print(response)
        controllers.pokemon_list.assert_called_once()
    
    @patch("src.rest.controllers.Controllers")
    def test_pokemon_healthcare(self, mock_controllers: MagicMock) -> None:
        """Test should call controllers pokemon healthcare method once"""
        controllers = mock_controllers.return_value
        controllers.pokemon_healthcare().return_value = MagicMock()
        response = self.tester.get('/pokemon/healthcare')
        print(response)
        controllers.pokemon_healthcare.assert_called_once()
    
    @patch("src.rest.controllers.Controllers")
    def test_trainer_adoption(self, mock_controllers: MagicMock) -> None:
        """Test should call controllers trainer adoption method once"""
        controllers = mock_controllers.return_value
        controllers.trainer_adoption().return_value = MagicMock()
        response = self.tester.post('/pokemon/adoption')
        print(response)
        controllers.trainer_adoption.assert_called_once()
    
    @patch("src.rest.controllers.Controllers")
    def test_trainer_status(self, mock_controllers: MagicMock) -> None:
        """Test should call controllers trainer status method once"""
        controllers = mock_controllers.return_value
        controllers.trainer_status().return_value = MagicMock()
        response = self.tester.get('/pokemon/status')
        print(response)
        controllers.trainer_status.assert_called_once()