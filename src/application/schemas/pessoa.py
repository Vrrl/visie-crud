from typing import Optional, Union, List
from pydantic import BaseModel, validator
from datetime import date

class PessoaSchema(BaseModel):
    nome: str
    rg: str
    cpf: str
    data_nascimento: date
    data_admissao: date
class ListPessoaSchema(BaseModel):
    nome: str
    data_admissao: date
    
    class Config:
        orm_mode = True