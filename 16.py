import math
print("Loja de Tintas")

area = float(input("Digite o tamanho da area a ser pintada em Metros²: "))

tintaLitros = area / 3
tintaLatas = math.ceil(tintaLitros / 18)
custoTotal = tintaLatas * 80.0

print(f"Você deverá comprar o total de: {tintaLatas} latas de tinta.")
print(f"O custo total é de: R${custoTotal:.2f}.")