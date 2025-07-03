from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.ProjetoCase.Update.UpdateProjetoCommand(BaseModel):
    id: str = None
    nome: str = None
    dataInicio: datetime = None
    dataFimPrevista: datetime = None
    statusProjeto: Any = None
    idSigfapes: int = None
    editalId: str = None