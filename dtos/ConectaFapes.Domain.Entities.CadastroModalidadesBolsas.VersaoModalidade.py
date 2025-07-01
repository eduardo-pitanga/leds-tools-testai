from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.CadastroModalidadesBolsas.VersaoModalidade(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    requisitoBolsas: List = None
    sigla: str
    descricao: str
    reducaoPorVinculo: float
    dataInicioVigencia: datetime = None
    dataFimVigencia: datetime = None
    estado: Any = None
    versaoModalidadeResolucaoId: str = None
    resolucao: Any = None
    versaoModalidadeModalidadeBolsaId: str = None
    modalidadeBolsa: Any = None
    modalidadeBolsaCompativeis: List = None
    versaoNiveis: List = None