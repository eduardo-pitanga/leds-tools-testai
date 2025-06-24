from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.CoordenacaoCase.Create.CreateCoordenacaoCommand(BaseModel):
    dataInicio: datetime = None
    dataFim: datetime = None
    pessoaId: str = None
    projetoId: str = None