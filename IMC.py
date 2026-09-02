"""
Algoritmo simples em Python para classificação de IMC e associação com potenciais
riscos à saúde. Desenvolvido para aplicar conceitos de lógica de programação e 
estruturas condicionais 
"""

import numpy as np 
import matplotlib.pyplot as pyplot

#eixo x
alturas = np.linspace(0.60, 2.72, 50)

#eixo y
baixo_peso  = 18.5 * (alturas ** 2)
peso_normal = 25 * (alturas ** 2)
sobrepeso   = 30 * (alturas ** 2)
obesidade_1 = 35 * (alturas ** 2)
obesidade_2 = 40 * (alturas ** 2)

plt.figure(figsize=(10,6))

plt.scatter(alturas, x, color="red", marker="0")

print("Índice de Massa Corporal (IMC)\n")


peso = input("Informe seu Peso (kg): ")
altura = input("Informe sua Altura em (Ex: 1.70): ")

peso = float(peso)
altura = float(altura)

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











