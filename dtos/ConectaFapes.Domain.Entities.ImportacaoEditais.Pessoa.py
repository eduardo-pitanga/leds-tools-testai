from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.Pessoa(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    nome: str = None
    cpf: str = None
    email: str = None
    dataNascimento: datetime = None
    nomeMae: str = None
    naturalidade: Any = None
    telefones: List = None
    documentos: List = None
    enderecos: List = None
    dadosBancarios: List = None
    alocacaoBolsistas: List = None
    coordenacaos: List = None
    estadoCivil: Any = None
    regimeCasamento: Any = None
    sexo: Any = None