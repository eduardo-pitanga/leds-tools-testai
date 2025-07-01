from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.DocumentoResponseDTO(BaseModel):
    id: str = None
    numero: str = None
    ufOrgaoEmissor: str = None
    orgaoEmissor: str = None
    dataEmissao: datetime = None
    pessoa: Any = None
    tipoDocumento: Any = None