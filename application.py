import os
import pandas as pd
from fastapi import FastAPI
from sqlalchemy import create_engine

app = FastAPI()
DATABASE_CONNECTION = f"mssql://{os.getenv('US')}:{os.getenv('PASSWORD')}@{os.getenv('SERVER')}/{os.getenv('DATABASE')}?driver={os.getenv('DRIVER')}"
# DATABASE_CONNECTION = 'mssql://SQL_server_office:12345678@IN3247868W1/Braniac_Marketing?driver=SQL Server Native Client 11.0'
print(DATABASE_CONNECTION)
engine = create_engine(DATABASE_CONNECTION)
connection = engine.raw_connection()

@app.get('/db')
def db():
    df = pd.read_sql_query('SELECT * FROM DEMOTB',con=connection)
    return df.head()

@app.get("/ping")
async def ping():
    return {"message": "pong"}
