"""
Database Schemas for Smart Notes Generator

Each Pydantic model below represents a MongoDB collection. The collection
name is the lowercase class name (e.g., Note -> "note").
"""
from __future__ import annotations
from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

class Folder(BaseModel):
    name: str = Field(..., description="Folder name")
    color: Optional[str] = Field(None, description="Hex color for UI tag")

class Note(BaseModel):
    title: str = Field(..., description="Note title")
    content: str = Field("", description="Rich text / Markdown content")
    source_type: Literal["text","file","url"] = Field(...)
    source_name: Optional[str] = None
    options: Dict[str, Any] = Field(default_factory=dict)
    folder_id: Optional[str] = None
    keywords: List[str] = Field(default_factory=list)
    topics: List[str] = Field(default_factory=list)
    transcript: Optional[str] = None

class Quiz(BaseModel):
    note_id: str
    title: str
    questions: List[Dict[str, Any]]

class Flashcard(BaseModel):
    note_id: str
    cards: List[Dict[str, str]]

class Setting(BaseModel):
    key: str
    value: Any
