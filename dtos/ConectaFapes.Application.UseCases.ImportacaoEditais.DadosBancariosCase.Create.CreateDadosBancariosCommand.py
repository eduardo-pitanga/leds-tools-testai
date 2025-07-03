from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.DadosBancariosCase.Create.CreateDadosBancariosCommand(BaseModel):
    conta: int = None
    agencia: int = None
    pessoaId: str = None
    bancoId: str = None