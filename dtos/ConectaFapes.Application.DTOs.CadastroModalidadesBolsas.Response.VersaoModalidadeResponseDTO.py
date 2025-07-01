from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.CadastroModalidadesBolsas.Response.VersaoModalidadeResponseDTO(BaseModel):
    id: str = None
    sigla: str = None
    descricao: str = None
    resolucao: Any = None
    modalidadeBolsa: Any = None
    versaoNiveis: List = None
    requisitoBolsas: List = None
    reducaoPorVinculo: float = None
    dataInicioVigencia: datetime = None
    dataFimVigencia: datetime = None
    estado: Any = None
    modalidadeBolsaCompativeis: List = None