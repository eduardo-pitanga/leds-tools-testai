from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ConectaFapes.Application.DTOs.ImportacaoEditais.Response.EnderecoResponseDTO(BaseModel):
    id: str = None
    logradouro: str = None
    numero: str = None
    complemento: str = None
    cep: str = None
    bairro: str = None
    municipio: str = None
    ufLocalidade: str = None