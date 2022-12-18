from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, status

from src.application.schemas import PessoaSchema

from src.application.services import PessoaService

router = APIRouter(tags=["pessoas"], prefix="/v1/pessoas")

@router.get("/")
def list_users(
    limit: Optional[int] = 100,
    start: Optional[int] = 0,
    pessoa_service: PessoaService = Depends(),
):
    """List Pessoas Route"""
    return pessoa_service.list(limit, start)


@router.post("/")
def list_users(
    pessoa: PessoaSchema,
    pessoa_service: PessoaService = Depends(),
):
    """Create Pessoas Route"""
    return pessoa_service.create(pessoa)


@router.put("/{pessoa_id}")
def list_users(
    pessoa_id: int,
    pessoa: PessoaSchema,
    pessoa_service: PessoaService = Depends(),
):
    """Edit Pessoas Route"""
    return pessoa_service.update(pessoa_id, pessoa)


@router.delete("/{pessoa_id}")
def list_users(
    pessoa_id: int,
    pessoa_service: PessoaService = Depends(),
):
    """Delete Pessoas Route"""
    return pessoa_service.delete(pessoa_id)
