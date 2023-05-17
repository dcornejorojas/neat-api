import unittest
from unittest.mock import AsyncMock, MagicMock, patch
from app import app
from src.rest.controllers import Controllers


class TestControllers(unittest.TestCase):
    def test_pokemon_list_empty_list(self):
        """Test should return empty unnadopted pokemon list (NOT IMPLEMENTED)"""
        pass
        