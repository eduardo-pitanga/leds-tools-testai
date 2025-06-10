from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Microsoft.OData.ODataFunctionImportInfo(BaseModel):
    typeAnnotation: Any = None
    url: str = None
    name: str = None
    title: str = None