
from pydantic import BaseModel, Field
from typing import Optional

class ClienteCreate(BaseModel):
    nome: str
    telefone: int
    correntista: bool
    saldo_cc: Optional[float] = None


class ClienteUpdate(BaseModel):
    nome: Optional[str] = Field(None, description="Nome do cliente")
    telefone: Optional[int] = Field(None, description="Telefone (apenas números)")
    correntista: Optional[bool] = Field(None, description="Cliente é correntista?")
    saldo_cc: Optional[float] = Field(None, description="Saldo da conta corrente")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"saldo_cc": 35.0},
                {"nome": "Leo"},
                {"telefone": 11999999999},
                {"correntista": False},
                {"nome": "Leo", "saldo_cc": 120.0}
            ]
        }
    }


class ClienteOut(BaseModel):
    id: int
    nome: str
    telefone: int
    correntista: bool
    saldo_cc: float
    score_credito: float


