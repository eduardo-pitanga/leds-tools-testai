from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.CadastroModalidadesBolsas.VersaoModalidadeCases.Update.UpdateVersaoModalidadeCommand(BaseModel):
    id: str = None
    resolucaoId: str = None
    modalidadeBolsaId: str = None
    sigla: str = None
    descricao: str = None
    reducaoPorVinculo: float = None
    dataInicioVigencia: datetime = None
    modalidadeBolsaCompativeis: List = None