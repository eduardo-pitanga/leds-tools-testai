from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Microsoft.OData.Edm.Vocabularies.IEdmTerm(BaseModel):
    type: Any = None
    appliesTo: str = None
    defaultValue: str = None
    schemaElementKind: Any = None
    namespace: str = None
    name: str = None