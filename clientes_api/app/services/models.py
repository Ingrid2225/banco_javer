from pydantic import BaseModel, EmailStr

class ContaModel(BaseModel):
    agencia: str
    numero_conta: str
    nome: str
    telefone: int
    cpf: str
    email: EmailStr
    correntista: bool
    saldo_cc: float
    cheque_especial_contratado: bool
    limite_cheque_especial: float
    limite_atual: float
    score_credito: float
