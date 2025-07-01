from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.CadastroModalidadesBolsas.ResolucaoCases.Create.CreateResolucaoCommand(BaseModel):
    numero: int = None
    data: datetime = None
    ementa: str = None
    link: str = None