from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.PlanejamentoNivelCase.Update.UpdatePlanejamentoNivelCommand(BaseModel):
    id: str = None
    quantidade: int = None
    planejamentoAlocacaoId: str = None
    versaoNivelId: str = None