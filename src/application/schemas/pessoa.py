from typing import Optional, Union, List
from pydantic import BaseModel, validator
from datetime import date, datetime

class PessoaSchema(BaseModel):
    nome: str
    rg: str
    cpf: str
    data_nascimento: date
    data_admissao: date
class ListPessoaSchema(BaseModel):
    id_pessoa: int
    nome: str
    data_admissao: date
    
    class Config:
        orm_mode = True
        
    @validator('nome')
    def first_name(cls, nome):
        return nome.split(" ")[0]
    
    @validator('data_admissao')
    def convert_date(cls, data_admissao):
        return data_admissao.strftime('%d/%m/%Y')