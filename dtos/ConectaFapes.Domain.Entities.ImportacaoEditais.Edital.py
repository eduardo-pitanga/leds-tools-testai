from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.Edital(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    nome: str
    dataCriacao: datetime
    dataUltimaSincronizacao: datetime = None
    idSigfapes: int
    editalAreaTecnicaId: str = None
    areaTecnica: Any = None
    projetos: List = None
    statusImportacao: Any