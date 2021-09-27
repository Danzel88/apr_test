from typing import List

from fastapi import Depends, HTTPException, status

from search import tables
from search.database import Session, get_session, es
from search.settings import setting


class PostsService:
    @classmethod
    async def search_text_in_es(cls, text: str):
        count_items = await es.count(index=setting.es_index)
        response = await es.search(index=setting.es_index,
                                   body={"query":
                                             {"match":
                                                  {"text": text}},
                                         "size": count_items['count']})
        id_list = []
        for i in response["hits"]["hits"]:
            id_list.append(int(i["_source"]["id"]))
        return id_list

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get_posts(self, text: str) -> List[tables.Posts]:
        post_id = await self.search_text_in_es(text)
        query = self.session.query(tables.Posts)
        in_exp = tables.Posts.id.in_(post_id)
        in_query = query.filter(in_exp)
        posts = in_query.order_by(tables.Posts.created_date.desc()).limit(20).all()
        return posts

    async def delete_post(self, post_id: int):
        post = self.session.query(tables.Posts).filter_by(id=post_id).first()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        self.session.delete(post)
        self.session.commit()
        await es.delete(index=setting.es_index, doc_type=setting.es_type, id=post_id)
        return post
