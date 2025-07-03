from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.Coordenacao(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    dataInicio: datetime = None
    dataFim: datetime = None
    coordenacaoPessoaId: str = None
    pessoa: Any = None
    coordenacaoProjetoId: str = None
    projeto: Any = None