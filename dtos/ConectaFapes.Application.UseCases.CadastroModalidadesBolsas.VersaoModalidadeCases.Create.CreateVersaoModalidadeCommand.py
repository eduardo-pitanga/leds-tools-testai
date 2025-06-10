from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.CadastroModalidadesBolsas.VersaoModalidadeCases.Create.CreateVersaoModalidadeCommand(BaseModel):
    resolucaoId: str = None
    modalidadeBolsaId: str = None
    sigla: str = None
    reducaoPorVinculo: float = None
    descricao: str = None
    dataInicioVigencia: datetime = None
    modalidadeBolsaCompativeis: List = None