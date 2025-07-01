from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.DadosBancariosCase.Update.UpdateDadosBancariosCommand(BaseModel):
    id: str = None
    conta: int = None
    agencia: int = None
    pessoaId: str = None
    bancoId: str = None