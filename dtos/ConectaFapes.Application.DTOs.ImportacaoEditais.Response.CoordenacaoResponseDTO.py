from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.CoordenacaoResponseDTO(BaseModel):
    id: str = None
    dataInicio: datetime = None
    dataFim: datetime = None
    pessoa: Any = None
    projeto: Any = None