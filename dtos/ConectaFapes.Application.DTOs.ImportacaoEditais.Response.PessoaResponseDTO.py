from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.PessoaResponseDTO(BaseModel):
    id: str = None
    nome: str = None
    cpf: str = None
    email: str = None
    dataNascimento: datetime = None
    nomeMae: str = None
    estadoCivil: Any = None
    regimeCasamento: Any = None
    sexo: Any = None
    naturalidade: Any = None
    endereco: Any = None
    telefones: List = None
    documentos: List = None
    dadosBancarios: List = None