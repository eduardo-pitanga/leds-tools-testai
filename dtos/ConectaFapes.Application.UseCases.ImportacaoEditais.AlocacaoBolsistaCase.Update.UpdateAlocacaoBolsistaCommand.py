from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.AlocacaoBolsistaCase.Update.UpdateAlocacaoBolsistaCommand(BaseModel):
    id: str = None
    inicioAtividade: datetime = None
    dataPrevistaFimAtividade: datetime = None
    dataFimAtividade: datetime = None
    dataSolicitacaoCancelamento: datetime = None
    qtdeCotas: int = None
    qtdeCotasPagas: int = None
    status: Any = None
    idSigfapes: int = None
    pessoaId: str = None
    projetoId: str = None
    versaoNivelId: str = None