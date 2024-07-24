import math

print("Loja de Tintas 2")

cobertura_por_litro = 6     #A cobertura considerada é 1 litro para cada 6 metros
litro_por_lata = 18
preco_por_lata = 80.0       #Preço por lata em reais
litro_por_galao = 3.6
preco_por_galao = 25.0      #Preço por galão em reais
per_folga = 0.10            #Percentual para acrescentar de folga 10%

area = float(input("Digite a quantidade de metros²: "))

#Calculo apenas latas de 18 litros
latas_necessarias = math.ceil((area / litro_por_lata) * (1 + per_folga))
custo_latas = latas_necessarias * preco_por_lata

#Calculo apenas galão de 3.6 litros
galoes_necessarios = math.ceil((area / litro_por_galao) * (1 + per_folga))
custo_galoes = galoes_necessarios * preco_por_galao

print("1. Considerando apenas latas de 18 litros.")
print(f" - Total de Latas de {litro_por_lata} litros: {latas_necessarias} latas")
print(f" - Custo total de: R${custo_latas:.2f}")

print("2. Considerando apenas galões de 3.6 litros.")
print(f" - Total de Latas de {litro_por_galao} litros: {galoes_necessarios} galão(s).")
print(f" - Custo total de: R${custo_galoes:.2f}")

