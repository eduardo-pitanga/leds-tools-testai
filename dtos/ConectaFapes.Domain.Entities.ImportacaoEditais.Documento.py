from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Domain.Entities.ImportacaoEditais.Documento(BaseModel):
    id: str = None
    dateCreated: datetime = None
    dateUpdated: datetime = None
    dateDeleted: datetime = None
    numero: str = None
    ufOrgaoEmissor: str = None
    orgaoEmissor: str = None
    dataEmissao: datetime = None
    tipoDocumento: Any = None
    documentoPessoaId: str = None
    pessoa: Any = None