from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.PlanejamentoNivelResponseDTO(BaseModel):
    id: str = None
    quantidade: int = None
    planejamentoAlocacao: Any = None
    versaoNivel: Any = None