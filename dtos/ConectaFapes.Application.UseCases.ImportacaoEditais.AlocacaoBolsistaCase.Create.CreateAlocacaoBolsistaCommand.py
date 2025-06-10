from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.AlocacaoBolsistaCase.Create.CreateAlocacaoBolsistaCommand(BaseModel):
    inicioAtividade: datetime = None
    dataPrevistaFimAtividade: datetime = None
    dataFimAtividade: datetime = None
    qtdeCotas: int = None
    status: Any = None
    idSigfapes: int = None
    pessoaId: str = None
    projetoId: str = None
    versaoNivelId: str = None