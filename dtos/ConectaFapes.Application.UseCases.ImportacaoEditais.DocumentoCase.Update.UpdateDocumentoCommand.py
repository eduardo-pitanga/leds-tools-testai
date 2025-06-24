from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.UseCases.ImportacaoEditais.DocumentoCase.Update.UpdateDocumentoCommand(BaseModel):
    id: str = None
    numero: str = None
    ufOrgaoEmissor: str = None
    orgaoEmissor: str = None
    dataEmissao: datetime = None
    tipoDocumento: Any = None
    pessoaId: str = None