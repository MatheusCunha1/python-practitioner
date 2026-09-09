"""
Algoritmo simples em Python para classificação de IMC e associação com potenciais
riscos à saúde. Desenvolvido para aplicar conceitos de lógica de programação e 
estruturas condicionais 
"""

# /// script
# dependencies = [
#     "numpy",
#     "matplotlib",
#     "requests",
# ]
# ///

import requests
import numpy as np 
import pandas as pd
import matplotlib.pyplot as pyplot




import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = ""

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "mustafaali96/weight-height",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())


pyplot.figure(figsize=(10,6))
pyplot.title("Gráfico de Dispersão - IMC")
pyplot.xlabel("Altura")
pyplot.ylabel("Peso")

alturas = np.linspace(0.60, 2.72, 100)

baixo_peso  = 18.5 * (alturas ** 2)
peso_normal = 25 * (alturas ** 2)
sobrepeso   = 30 * (alturas ** 2)
obesidade_1 = 35 * (alturas ** 2)
obesidade_2 = 40 * (alturas ** 2)

pyplot.fill_betweenx(alturas, 0, baixo_peso, color="lightblue", alpha=0.3, label="Abaixo do Peso", linestyle="--")
pyplot.fill_betweenx(alturas, baixo_peso, peso_normal, color="green", alpha=0.4, label="Peso Normal",  linestyle="--")
pyplot.fill_betweenx(alturas, peso_normal, sobrepeso, color="yellow", alpha=0.5, label="Sobrepeso",  linestyle="--")
pyplot.fill_betweenx(alturas, sobrepeso, obesidade_1, color="orange", alpha=0.6, label="Obesidade Grau I",  linestyle="--")
pyplot.fill_betweenx(alturas, obesidade_1, obesidade_2, color="red", alpha=0.7, label="Obesidade Grau II", linestyle="--")


peso = input("Informe seu Peso (kg): ") 
altura = input("Informe sua Altura em (Ex: 1.70): ")

peso = float(peso)
altura = float(altura)

pyplot.scatter(peso, altura, color="black", marker="o", s=100, zorder=5, label="Vc esta aqui")

pyplot.ylim(min(alturas), max(alturas))
pyplot.xlim(min(baixo_peso), max(obesidade_2))

pyplot.show()

print("Índice de Massa Corporal (IMC)\n")


imc = peso / (altura ** 2)

print("\nSeu IMC é:", int(imc))

if imc < 18.5:
    print("|Baixo peso| Fadiga, estresse, perda de cabelo")
elif 18.5 <= imc < 25: 
    print("|Peso normal| Menor risco de doenças")
elif 25 <= imc < 30: 
    print("|Sobrepeso| Fadiga, má circulação, varizes")
elif 30 <= imc < 35: 
    print("|Obesidade Grau I| Diabetes, infarto, angina")
elif 35 <= imc < 40: 
    print("|Obesidade Grau II| Apneia do sono, falta de ar")
else:
    print("|Obesidade Grau III| Refluxo, infarto, AVC, dificuldades de locomoção")











