from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.EnderecoCase.Create.CreateEnderecoCommand(BaseModel):
    logradouro: str = None
    numero: str = None
    complemento: str = None
    cep: str = None
    bairro: str = None
    municipio: str = None
    ufLocalidade: str = None
    pessoaId: str = None