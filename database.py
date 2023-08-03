# pip install databases sqlalchemy asyncpg psycopg2-binary
from databases import Database
from sqlalchemy import (MetaData,
                        create_engine,
                        Table,
                        Column,
                        Integer,
                        Identity,
                        String,
                        Text,
                        DateTime,
                        func,
                
                        )

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'


database = Database(DATABASE_URL)
metadata = MetaData()

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, Identity(), primary_key = True),
    Column('title',String),
    Column('context',Text),
    Column('author', String),
    Column('location',String),
    Column('created_at',DateTime, server_default_func = func.now()),
    Column('updated_at',DateTime, onupdate = func.now())   
)
engine =create_engine(DATABASE_URL)

metadata.create_all(engine)