valor = input("Digite um valor em Metros para conversão em Centímetros: ")
converter = float(valor.replace(",",".")) * 100

print(f" O valor: {valor} metros, convertido para centimetros é: {converter} centímetros")