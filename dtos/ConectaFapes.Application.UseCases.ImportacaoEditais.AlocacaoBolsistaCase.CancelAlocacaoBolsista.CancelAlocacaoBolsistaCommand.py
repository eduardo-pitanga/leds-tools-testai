from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.AlocacaoBolsistaCase.CancelAlocacaoBolsista.CancelAlocacaoBolsistaCommand(BaseModel):
    id: str = None
    dataFimAtividade: datetime = None
    justificativaCancelamento: str = None