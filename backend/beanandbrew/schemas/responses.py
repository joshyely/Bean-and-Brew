from pydantic import BaseModel
from .token import Token

class Detail(BaseModel):
    detail: str