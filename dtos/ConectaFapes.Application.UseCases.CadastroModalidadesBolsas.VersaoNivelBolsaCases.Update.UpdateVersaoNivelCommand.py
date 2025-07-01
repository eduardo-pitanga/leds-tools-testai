from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.CadastroModalidadesBolsas.VersaoNivelBolsaCases.Update.UpdateVersaoNivelCommand(BaseModel):
    id: str = None
    valor: float = None
    nivelBolsaId: str = None
    versaoModalidadeId: str = None
    moedaId: str = None