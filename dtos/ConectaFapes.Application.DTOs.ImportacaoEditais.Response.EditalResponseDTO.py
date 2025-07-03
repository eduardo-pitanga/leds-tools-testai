from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.EditalResponseDTO(BaseModel):
    id: str = None
    nome: str = None
    dataCriacao: datetime = None
    dataUltimaSincronizacao: datetime = None
    idSigfapes: int = None
    statusImportacao: Any = None
    projetos: List = None
    areaTecnica: Any = None