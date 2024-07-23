print("Calcule números inteiros e real")

numInt1 = int(input("Digite um número inteiro: "))
numInt2 = int(input("Digite um segundo número inteiro: "))
numReal = float(input("Digite um número real: "))

dobroInt1 = numInt1 * 2
metadeInt2 = numInt2 / 2

#Multiplica o dobro do primeiro pela metade do segundo.
multipInt = dobroInt1 * metadeInt2

#Soma do triplo do primeiro com o terceiro.
somaTrip = (numInt1 * 3) + numReal

#Terceiro número elevado ao cubo.
elevCubo = numReal ** 3

print(f"a. O Produto do dobro do primeiro com metade do segundo: {multipInt}")
print(f"b. A Soma do triplo do primeiro com o terceiro: {somaTrip}")
print(f"c. Terceiro número elevado ao cubo: {elevCubo}")
