print("Calcula Holerite")

valorHora = float(input("Digite o Valor da sua hora Trabalhada: "))
horaTrabalhada = float(input("Informe o número de horas trabalhadas: "))

#Definindo Deduções
ir = 0.11
inss = 0.08
sindicato = 0.05

salarioBruto = valorHora * horaTrabalhada
descIr = salarioBruto * ir
descInss = salarioBruto * inss
descSind = salarioBruto * sindicato
descTotal = descIr + descInss + descSind
salarioLiquido = salarioBruto - descTotal

print(f"+ Salário Bruto: R${salarioBruto:.2f}")
print(f" - IR: R${descIr:.2f}")
print(f" - INSS: R${descInss:.2f}")
print(f" - Sindicato: R${descSind:.2f}")
print(f"= Salário Liquido: R${salarioLiquido:.2f}")
