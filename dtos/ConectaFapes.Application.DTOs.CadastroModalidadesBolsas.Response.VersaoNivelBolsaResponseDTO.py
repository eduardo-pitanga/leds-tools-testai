from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response.VersaoNivelBolsaResponseDTO(BaseModel):
    id: str = None
    valor: float = None
    nivelBolsa: Any = None
    moeda: Any = None
    versaoModalidade: Any = None
    requisitoBolsas: List = None
    alocacaoBolsistas: List = None