import math

print("Loja de Tintas 2")

# Constantes
cobertura_por_litro = 6     # A cobertura considerada é 1 litro para cada 6 metros quadrados
litro_por_lata = 18
preco_por_lata = 80.0       # Preço por lata em reais
litro_por_galao = 3.6
preco_por_galao = 25.0      # Preço por galão em reais
per_folga = 0.10            # Percentual para acrescentar de folga 10%

area = float(input("Digite a quantidade de metros²: "))

# Calculo da quantidade de tinta necessária com folga
tinta_necessaria = math.ceil((area / cobertura_por_litro) * (1 + per_folga))

# Calculo apenas latas de 18 litros
latas_necessarias = math.ceil(tinta_necessaria / litro_por_lata)
custo_latas = latas_necessarias * preco_por_lata

# Calculo apenas galões de 3.6 litros
galoes_necessarios = math.ceil(tinta_necessaria / litro_por_galao)
custo_galoes = galoes_necessarios * preco_por_galao

# Inicializa o melhor custo como infinito para garantir que qualquer custo encontrado será menor
melhor_custo = float('inf')
melhor_comb = None

# Loop para encontrar a melhor combinação de latas e galões
for latas in range(math.ceil(tinta_necessaria / litro_por_lata) + 1):
    litros_com_latas = latas * litro_por_lata
    litros_restantes = tinta_necessaria - litros_com_latas
    if litros_restantes > 0:
        galoes = math.ceil(litros_restantes / litro_por_galao)
    else:
        galoes = 0
    custo_total = latas * preco_por_lata + galoes * preco_por_galao
    if custo_total < melhor_custo:
        melhor_custo = custo_total
        melhor_comb = (latas, galoes)

# Impressão dos resultados
print("1. Considerando apenas latas de 18 litros.")
print(f" - Total de Latas de {litro_por_lata} litros: {latas_necessarias} latas")
print(f" - Custo total de: R${custo_latas:.2f}")

print("2. Considerando apenas galões de 3.6 litros.")
print(f" - Total de Galões de {litro_por_galao} litros: {galoes_necessarios} galão(ões)")
print(f" - Custo total de: R${custo_galoes:.2f}")

print("3. Misturando latas e galões (menor desperdício de tinta):")
print(f"   - Quantidade de latas: {melhor_comb[0]}")
print(f"   - Quantidade de galões: {melhor_comb[1]}")
print(f"   - Custo total é de: R${melhor_custo:.2f}")
