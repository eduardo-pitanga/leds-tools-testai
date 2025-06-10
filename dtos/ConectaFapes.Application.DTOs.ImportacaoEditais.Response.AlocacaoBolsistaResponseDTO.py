from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.AlocacaoBolsistaResponseDTO(BaseModel):
    id: str = None
    inicioAtividade: datetime = None
    dataPrevistaFimAtividade: datetime = None
    dataFimAtividade: datetime = None
    dataSolicitacaoCancelamento: datetime = None
    justificativaCancelamento: str = None
    qtdeCotas: int = None
    qtdeCotasPagas: int = None
    status: Any = None
    idSigfapes: int = None
    pessoa: Any = None
    projeto: Any = None
    versaoNivel: Any = None