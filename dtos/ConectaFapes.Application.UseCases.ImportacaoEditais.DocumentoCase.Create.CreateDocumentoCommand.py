from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.DocumentoCase.Create.CreateDocumentoCommand(BaseModel):
    numero: str = None
    ufOrgaoEmissor: str = None
    orgaoEmissor: str = None
    dataEmissao: datetime = None
    tipoDocumento: Any = None
    pessoaId: str = None