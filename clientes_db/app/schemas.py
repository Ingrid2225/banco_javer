
from pydantic import BaseModel, Field, ConfigDict

class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=2)
    telefone: int
    correntista: bool
    saldo_cc: float | None = None

class ClienteUpdate(BaseModel):
    nome: str | None = None
    telefone: int | None = None
    correntista: bool | None = None
    saldo_cc: float | None = None

class ClienteOut(BaseModel):
    id: int
    nome: str
    telefone: int
    correntista: bool
    saldo_cc: float


    model_config = ConfigDict(from_attributes=True)
