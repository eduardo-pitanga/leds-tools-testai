from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.Projeto(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    nome: str
    dataInicio: datetime
    dataFimPrevista: datetime
    idSigfapes: int
    alocacoesCompletas: int = None
    statusPreenchimento: Any
    statusProjeto: Any
    coordenadores: List = None
    planejamentoAlocacao: Any = None
    projetoEditalId: str = None
    edital: Any = None
    alocacaoBolsistas: List = None