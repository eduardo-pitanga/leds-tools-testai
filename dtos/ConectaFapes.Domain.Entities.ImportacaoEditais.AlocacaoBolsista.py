from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.AlocacaoBolsista(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    inicioAtividade: datetime = None
    dataPrevistaFimAtividade: datetime = None
    dataFimAtividade: datetime = None
    dataSolicitacaoCancelamento: datetime = None
    justificativaCancelamento: str = None
    qtdeCotas: int = None
    qtdeCotasPagas: int = None
    status: Any = None
    idSigfapes: int = None
    alocacaoBolsistaPessoaId: str = None
    pessoa: Any = None
    alocacaoBolsistaProjetoId: str = None
    projeto: Any = None
    alocacaoBolsistaVersaoNivelId: str = None
    versaoNivel: Any = None