from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.domain.trainer.trainer import Trainer
from src.domain.pokemon.pokemon import Pokemon

class Adoption(BaseModel):
    date: datetime
    pokemon: Pokemon
    trainer: Trainer
    status: str
    description: str