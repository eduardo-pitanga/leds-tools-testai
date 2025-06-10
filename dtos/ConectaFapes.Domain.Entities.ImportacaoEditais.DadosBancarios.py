from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.DadosBancarios(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    conta: int = None
    agencia: int = None
    dadosBancariosPessoaId: str = None
    pessoa: Any = None
    dadosBancariosBancoId: str = None
    banco: Any = None