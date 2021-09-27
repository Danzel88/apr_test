from typing import List

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from search.models.posts import BasePosts
from search.services.posts import PostsService

router = APIRouter(prefix='')
templates = Jinja2Templates(directory='templates')


@router.get('/', response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@router.get('/search', response_model=List[BasePosts])
async def search_posts(search_text, service: PostsService = Depends()):
    result = await service.get_posts(search_text)
    return result


@router.get('/delete')
async def delete_post(post_id: int, service: PostsService = Depends()):
    result = await service.delete_post(post_id)
    return result
