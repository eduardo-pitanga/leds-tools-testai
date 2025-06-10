from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.CadastroModalidadesBolsas.RequisitoBolsa(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    tipo: Any
    descricao: str
    requisitoBolsaVersaoId: str = None
    versao: Any = None