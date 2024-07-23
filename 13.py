print("Calcule o peso ideal por Feminino/Masculino")

altura = float(input("Digite a sua altura: "))
sexo = int(input("Informe seu Sexo: 1 - Masculino ou 2 - Feminino: "))

if sexo == 1:
    pesoIdeal = (72.7*altura) -58
    print(f"Seu sexo é Masculino, peso ideal: {pesoIdeal}")
elif sexo == 2:
    pesoIdeal = (62.1*altura) -44.7
    print(f"Seu sexo é Feminino, peso ideal: {pesoIdeal}")
else:
    print(" Sexo Invalido! Digite 1 - Masculino ou 2 - Feminino.")
