from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.PlanejamentoAlocacaoCase.Update.UpdatePlanejamentoAlocacaoCommand(BaseModel):
    id: str = None
    data: datetime = None
    projetoId: str = None