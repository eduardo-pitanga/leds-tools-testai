from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Microsoft.OData.Edm.IEdmSchemaElement(BaseModel):
    schemaElementKind: Any = None
    namespace: str = None
    name: str = None