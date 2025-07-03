from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.AreaTecnicaResponseDTO(BaseModel):
    id: str = None
    nome: str = None
    descricao: str = None
    editais: List = None