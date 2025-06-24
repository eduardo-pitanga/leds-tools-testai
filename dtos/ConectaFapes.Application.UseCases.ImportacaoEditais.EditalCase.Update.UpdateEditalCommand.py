from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.EditalCase.Update.UpdateEditalCommand(BaseModel):
    id: str = None
    nome: str = None
    areaTecnicaId: str = None
    dataCriacao: datetime = None
    idSigfapes: int = None