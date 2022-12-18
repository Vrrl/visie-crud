from fastapi import Depends, HTTPException, status

from src.infra.db.sqlalchemy.entities import Pessoa

from src.infra.db.sqlalchemy.repository import PesssoaRepository

from src.application.schemas import PessoaSchema

from typing import List, Optional


class PessoaService:
    pessoa_repository: PesssoaRepository

    def __init__(self, pessoa_repository: PesssoaRepository = Depends()) -> None:
        self.pessoa_repository = pessoa_repository
        
    def create(self, pessoa_body: PessoaSchema) -> Pessoa:
        return self.pessoa_repository.add(
            Pessoa(
                nome=pessoa_body.nome,
                rg=pessoa_body.rg,
                cpf=pessoa_body.cpf,
                data_nascimento=pessoa_body.data_nascimento,
                data_admissao=pessoa_body.data_admissao
            )
        )

    def delete(self, pessoa_id: int) -> None:
        self.pessoa_repository.delete(id=pessoa_id)

    def list(self, limit: Optional[int] = 100, start: Optional[int] = 0) -> List[Pessoa]:
        return self.pessoa_repository.list(limit, start)

    def update(self, pessoa_id: str, new_pessoa_body: PessoaSchema) -> Pessoa:
        return self.pessoa_repository.edit(
            pessoa_id, 
            Pessoa(
                nome=new_pessoa_body.nome,
                rg=new_pessoa_body.rg,
                cpf=new_pessoa_body.cpf,
                data_nascimento=new_pessoa_body.data_nascimento,
                data_admissao=new_pessoa_body.data_admissao
            )
        )

    