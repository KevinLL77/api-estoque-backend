# schemas.py
from pydantic import BaseModel
from typing import Optional

# Base para criar e atualizar produtos
class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade_estoque: int

class ProdutoCreate(ProdutoBase):
    pass

# Modelo de resposta (inclui o ID gerado pelo banco)
class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True