import duckdb 
from pathlib import Path

conect = duckdb.connect()

silver = Path(r"../data/silver").iterdir()

def create_view(conect, silver): 
    for arquivo in silver: 
        conect.sql(f""" 
            CREATE OR REPLACE VIEW VW_{arquivo.stem} AS 
                SELECT * FROM {str(arquivo)} 
        """)