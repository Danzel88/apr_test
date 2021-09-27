from datetime import datetime

from pydantic import BaseModel


class BasePosts(BaseModel):
    id: int
    rubrics: str
    text: str
    created_date: datetime

    class Config:
        orm_mode = True
