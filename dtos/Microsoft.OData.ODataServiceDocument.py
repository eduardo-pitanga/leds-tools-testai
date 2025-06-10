from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Microsoft.OData.ODataServiceDocument(BaseModel):
    typeAnnotation: Any = None
    entitySets: List = None
    singletons: List = None
    functionImports: List = None