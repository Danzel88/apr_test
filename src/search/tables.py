import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Posts(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    rubrics = sa.Column(sa.String)
    text = sa.Column(sa.Text)
    created_date = sa.Column(sa.DateTime)
