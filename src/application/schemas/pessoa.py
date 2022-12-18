from typing import Optional, Union, List
from pydantic import BaseModel, validator


class PessoaSchema(BaseModel):
    name: str
    docker_image: str
    parameters: list
    