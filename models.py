from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Enum, Float, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())

    author_id = Column(Integer, ForeignKey("author.id"))
    author = relationship("Author")

    
class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)