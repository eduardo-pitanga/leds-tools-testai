from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.CadastroModalidadesBolsas.NivelBolsa(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    sigla: str
    versaoNiveis: List = None