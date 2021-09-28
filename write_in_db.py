import os
import asyncio

import httpx
import pandas as pd
import psycopg2


MAIN_URL = f"http://localhost:9200/apr_search/all_req/"
USER = os.getlogin()

data = pd.read_csv('posts.csv')
df = pd.DataFrame(data, columns=['text', 'created_date', 'rubrics'])


async def write_in_es(dataframe):
    print("Start writing in Elasticsearch")
    for el in dataframe.itertuples():
        article_id = el[0] + 1
        text = el[1]
        async with httpx.AsyncClient() as client:
            await client.post(f"{MAIN_URL}{article_id}", json={
                "id": f"{article_id}",
                "text": f"{text}"})
    print("ES done!")


async def write_in_postgres(dataframe):
    print("Start writing in Postgres")
    conn = psycopg2.connect(f"dbname=apr_test user={USER}")

    with conn:
        with conn.cursor() as curs:
            for row in dataframe.itertuples():
                curs.execute("""
                INSERT INTO posts (rubrics, text, created_date)
                VALUES (%s, %s, %s)
                """, (row.rubrics, row.text, row.created_date))
    print("POSTGRES done!")


async def main(dataframe):
    task_es = asyncio.create_task(write_in_es(dataframe))
    task_psql = asyncio.create_task(write_in_postgres(dataframe))
    await task_es
    await task_psql


if __name__ == '__main__':
    asyncio.run(main(df))
