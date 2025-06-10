from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.CoordenacaoCase.Update.UpdateCoordenacaoCommand(BaseModel):
    id: str = None
    dataInicio: int = None
    dataFim: int = None
    pessoaId: str = None
    projetoId: str = None