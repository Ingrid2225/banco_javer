
from pydantic import BaseModel, Field, EmailStr, confloat, ConfigDict
from typing import Optional

class ContaCreateIn(BaseModel):
    agencia: str = Field(..., min_length=3, max_length=4, pattern=r"^\d{3,4}$")
    numero_conta: str = Field(..., min_length=4, max_length=8, pattern=r"^\d{4,8}$")
    nome: str
    cpf: str = Field(..., min_length=11, max_length=11, pattern=r"^\d{11}$")
    telefone: int = Field(..., ge=1000000000, le=99999999999)
    email: EmailStr
    correntista: bool = True
    saldo_cc: Optional[float] = 0.0
    cheque_especial_contratado: bool = False
    limite_cheque_especial: Optional[float] = 0.0

class ContaUpdateIn(BaseModel):
    model_config = ConfigDict(extra="forbid")
    nome: Optional[str] = None
    cpf: Optional[str] = Field(None, min_length=11, max_length=11, pattern=r"^\d{11}$")
    telefone: Optional[int] = Field(None, ge=1000000000, le=99999999999)
    email: Optional[EmailStr] = None
    correntista: Optional[bool] = None

class OperacaoPorChavesIn(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    agencia: str = Field(..., min_length=3, max_length=4, pattern=r"^\d{3,4}$")
    numero_conta: str = Field(..., min_length=4, max_length=8, pattern=r"^\d{4,8}$")
    valor: confloat(gt=0) = Field(..., alias="saldo")

class ChequeEspecialCadastroIn(BaseModel):
    habilitado: bool
    limite: confloat(ge=0)
