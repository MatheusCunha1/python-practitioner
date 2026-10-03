import duckdb 
from pathlib import Path

def create_view(con, pasta = Path(r"../data/silver")): 

    pasta = pasta.iterdir()

    for arquivo in pasta: 
        con.sql(f""" 
            CREATE OR REPLACE VIEW VW_{arquivo.stem} AS 
                SELECT * FROM '{str(arquivo)}' 
        """)