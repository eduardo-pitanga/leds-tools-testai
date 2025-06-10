from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.PlanejamentoAlocacao(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    data: datetime = None
    planejamentoAlocacaoProjetoId: str = None
    projeto: Any = None
    planejamentoNivels: List = None