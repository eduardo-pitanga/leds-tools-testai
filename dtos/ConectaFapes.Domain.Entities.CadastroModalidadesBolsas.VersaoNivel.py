from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.CadastroModalidadesBolsas.VersaoNivel(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    requisitoBolsas: List = None
    valor: float = None
    versaoNivelNivelBolsaId: str = None
    nivelBolsa: Any = None
    versaoNivelVersaoModalidadeId: str = None
    versaoModalidade: Any = None
    versaoNivelMoedaId: str = None
    moeda: Any = None
    alocacaoBolsistas: List = None