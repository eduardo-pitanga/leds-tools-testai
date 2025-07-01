from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Microsoft.OData.Edm.IEdmModel(BaseModel):
    schemaElements: List = None
    vocabularyAnnotations: List = None
    referencedModels: List = None
    declaredNamespaces: List = None
    directValueAnnotationsManager: Any = None
    entityContainer: Any = None