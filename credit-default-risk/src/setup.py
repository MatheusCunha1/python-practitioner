import kagglehub
import shutil
from pathlib import Path  

path = kagglehub.competition_download('home-credit-default-risk')

print("Path to competition files:", path)

diretorio = Path.home() / ".cache" / "kagglehub" / "competitions" / "home-credit-default-risk"

destino = Path("../data")

destino.mkdir(parents=True)

for arquivo in diretorio.glob("*.csv"):
    shutil.move(str(arquivo), str(destino / arquivo.name)) 