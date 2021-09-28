from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from elasticsearch import AsyncElasticsearch

from search.settings import setting

engine = create_engine(setting.database_url)


Session = sessionmaker(engine, autocommit=False, autoflush=False)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()


# es = AsyncElasticsearch(f"http://{setting.es_user}:{setting.es_password}@localhost:9200/")
es = AsyncElasticsearch(f"http://localhost:9200/")

