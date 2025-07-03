from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.PlanejamentoNivel(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    quantidade: int = None
    planejamentoNivelPlanejamentoAlocacaoId: str = None
    planejamentoAlocacao: Any = None
    planejamentoNivelVersaoNivelId: str = None
    versaoNivel: Any = None