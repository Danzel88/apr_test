from fastapi import APIRouter

from .posts import router as posts_router

router = APIRouter()

router.include_router(posts_router)

