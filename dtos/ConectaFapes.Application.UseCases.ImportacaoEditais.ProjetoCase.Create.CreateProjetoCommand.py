from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.ProjetoCase.Create.CreateProjetoCommand(BaseModel):
    nome: str = None
    dataInicio: datetime = None
    dataFimPrevista: datetime = None
    idSigfapes: int = None
    statusProjeto: Any = None
    editalId: str = None