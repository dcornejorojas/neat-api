from pydantic import BaseModel
from datetime import datetime
from typing import List, Literal, Optional


class Trainer(BaseModel):
    name: str
    lastname: str
    address: str
    dni: str
    adopted_before: bool
    blocked: bool
    block_date: Optional[datetime]
    init_date: Optional[datetime]
    extra: str