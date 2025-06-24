from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response.ResolucaoResponseDTO(BaseModel):
    id: str = None
    numero: int = None
    data: datetime = None
    ementa: str = None
    link: str = None
    versaoModalidadesBolsas: List = None