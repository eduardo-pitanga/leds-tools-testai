from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response.ModalidadeBolsaResponseDTO(BaseModel):
    id: str = None
    sigla: str = None
    nome: str = None
    versaoModalidadesBolsas: List = None