from models.language import (TokenizationRequest,
                             TokenizationResponse,
                             StemmingRequest,
                             StemmingResponse)
from services import language
from fastapi.routing import APIRouter

language_router = APIRouter(
    prefix="/language",
     tags=["language"]
)

@language_router.post("/tokens")
async def tokenize_text(
    tokenizationDto: TokenizationRequest
) -> TokenizationResponse:
    return TokenizationResponse(
        tokens=language.tokenize_text(tokenizationDto.text)
    )

@language_router.post("/stems")
async def extract_stems(
    request: StemmingRequest
) -> StemmingResponse:
    return StemmingResponse(
        stems=language.extract_stems(request.text)
    )
