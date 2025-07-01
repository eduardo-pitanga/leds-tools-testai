from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.NaturalidadeCase.Create.CreateNaturalidadeCommand(BaseModel):
    cidade: str = None
    uf: str = None
    pessoaId: str = None