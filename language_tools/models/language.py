from pydantic import BaseModel
from typing import List

class TokenizationRequest(BaseModel):
    language: str
    text: str

class TokenizationResponse(BaseModel):
    tokens: List[str]

class StemmingRequest(BaseModel):
    text: str
    language: str

class StemmingResponse(BaseModel):
    stems: List[str]
