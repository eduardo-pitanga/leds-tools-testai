from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.DadosBancariosResponseDTO(BaseModel):
    id: str = None
    conta: int = None
    agencia: int = None
    pessoa: Any = None
    banco: Any = None