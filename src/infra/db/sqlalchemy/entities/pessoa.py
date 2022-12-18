import uuid

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
    Integer,
    Date
)

from src.infra.db.sqlalchemy.base import Base


class Pessoa(Base):
    """Model class of Sqlachemy"""

    __tablename__ = "pessoas"

    id_pessoa = Column(Integer, primary_key=True)

    nome = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    data_admissao = Column(Date, nullable=False)
    funcao = Column(String)
