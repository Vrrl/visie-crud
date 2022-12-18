from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.schemas import PessoaSchema, ListPessoaSchema

from src.application.services import PessoaService

router = APIRouter(tags=["pessoas"], prefix="/v1/pessoas")

@router.get("/", response_model=List[ListPessoaSchema])
def list_pessoas(
    limit: Optional[int] = 100,
    start: Optional[int] = 0,
    pessoa_service: PessoaService = Depends(),
):
    """List Pessoas Route"""
    return pessoa_service.list(limit, start)


@router.post("/")
def create_pessoa(
    pessoa: PessoaSchema,
    pessoa_service: PessoaService = Depends(),
):
    """Create Pessoas Route"""
    return pessoa_service.create(pessoa)


@router.put("/{pessoa_id}")
def update_pessoa(
    pessoa_id: int,
    pessoa: PessoaSchema,
    pessoa_service: PessoaService = Depends(),
):
    """Edit Pessoas Route"""
    return pessoa_service.update(pessoa_id, pessoa)


@router.delete("/{pessoa_id}")
def delete_pessoa(
    pessoa_id: int,
    pessoa_service: PessoaService = Depends(),
):
    """Delete Pessoas Route"""
    return pessoa_service.delete(pessoa_id)
