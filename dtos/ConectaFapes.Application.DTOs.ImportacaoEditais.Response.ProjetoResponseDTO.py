from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.ProjetoResponseDTO(BaseModel):
    id: str = None
    nome: str = None
    dataInicio: datetime = None
    dataFimPrevista: datetime = None
    idSigfapes: int = None
    alocacoesCompletas: int = None
    statusProjeto: Any = None
    statusPreenchimento: Any = None
    planejamentoAlocacao: Any = None
    edital: Any = None
    coordenadores: List = None
    alocacaoBolsistas: List = None
    planejamentoAlocacaos: List = None