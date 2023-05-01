# Handles the connection to database

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import time
import psycopg2
from psycopg2.extras import RealDictCursor


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# The engine is responsible for establishing a connection between sqlachemy and the database(prosgresql)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# The session is responsible for when you actual want to communicate with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# creating a dependency that creates a session when a request is sent to the database and closes the session after creating the request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:

#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'juzzy', cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print ("connection to database successful")

#         break
#     except Exception as error:
        
#         print('connection to database failed', error) 
#         time.sleep(2)