from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class BookOut(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
