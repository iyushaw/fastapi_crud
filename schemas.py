from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

class PostSchema(BaseModel):
    title: str
    author_id: int
    content: Text

    class Config:
        from_attributes = True

class UpdatePostSchema(BaseModel):
    title: str
    content: Text

    class Config:
        from_attributes = True

class AuthorSchema(BaseModel):
    name: Optional[str]
    age: Optional[int]
    rating: Optional[int]

    class Config:
        from_attributes = True

class UpdateAuthorSchema(BaseModel):
    name: Optional[str]
    age: Optional[int]
    rating: Optional[str]
    last_updated: datetime

    class Config:
        from_attributes = True