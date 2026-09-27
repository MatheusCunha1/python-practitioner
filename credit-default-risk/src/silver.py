import pandas as pd
import zipfile 
from pathlib import Path

arquivos = Path(r"../data/bronze").glob("*.csv")

for arquivo in arquivos:

    parquet = Path(r"../data/silver/" + arquivo.stem + ".parquet")

    if not parquet.exists(): 
        df = pd.read_csv(arquivo, encoding="latin1") 
        df.to_parquet(parquet)
  

    else: 
        with zipfile.ZipFile(r"../data/bronze/" + arquivo.stem + ".zip",  mode="w") as arquivo_zip:
            arquivo_zip.write(arquivo)
        
            arquivo.unlink()




