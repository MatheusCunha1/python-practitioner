peso = input("Informe seu Peso (kg): ")
altura = input("Informe sua Altura em (Ex: 1.70): ")

peso = float(peso)
altura = float(altura)

imc = peso / (altura ** 2)

print("Seu IMC é:", int(imc))


if imc < 18.5:
    print("| Baixo peso | Fadiga, estresse, perda de cabelo1")
elif imc >= 18.5 and 24.5: 
    print("| Peso normal | Menor risco de doenças")
elif imc >= 25 and 29.9: 
    print("| Sobrepeso | Fadiga, má circulação, varizes")
elif imc >= 30 and 34.9: 
    print("| Obesidade Grau I | Diabetes, infarto, angina")
elif imc >= 35.9 and 39.9: 
    print("| Obesidade Grau II | Apneia do sono, falta de ar")
else:
    print("| Obesidade Grau III | Refluxo, infarto, AVC, dificuldades de locomoção")












