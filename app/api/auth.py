from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])

@router.get("/test")
async def test():
    return {"test": "test"}