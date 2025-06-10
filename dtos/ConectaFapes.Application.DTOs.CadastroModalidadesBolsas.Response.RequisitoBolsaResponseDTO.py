from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response.RequisitoBolsaResponseDTO(BaseModel):
    id: str = None
    tipo: Any = None
    descricao: str = None
    versaoModalidade: Any = None
    versaoNivel: Any = None