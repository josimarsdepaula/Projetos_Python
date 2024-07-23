print("Calculadora Regulamento de Pesca")

pesoPeixe = float(input("Digite o peso dos Peixes: "))

limite = 50.0
multaPorQuilo = 4.0

if pesoPeixe > limite:
    excesso = pesoPeixe - limite
    multa = excesso * multaPorQuilo

else:
    excesso = 0
    multa = 0

print(f"O Peso total dos peixes é: {pesoPeixe:.2f}")
print(f"O Excesso de peso foi: {excesso:.2f}")
print(f"O valor total da multa é: R${multa:.2f}")