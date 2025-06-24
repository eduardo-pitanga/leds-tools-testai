from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.PessoaCase.Create.CreatePessoaCommand(BaseModel):
    nome: str = None
    cpf: str = None
    email: str = None
    dataNascimento: datetime = None
    nomeMae: str = None
    estadoCivil: Any = None
    regimeCasamento: Any = None
    sexo: Any = None