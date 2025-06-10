from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.EditalCase.Create.CreateEditalCommand(BaseModel):
    nome: str = None
    dataCriacao: datetime = None
    idSigfapes: int = None