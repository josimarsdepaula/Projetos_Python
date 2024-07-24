print("Converter MB")

tamanho_arquivo = float(input("Insira o tamanho do arquivo para donwload em (MB):"))
velocidade_internet = float(input("Insira a velocidade da conexão da sua internet em (Mbps):"))

converte_internet = velocidade_internet / 8
tempo_donwload = tamanho_arquivo / converte_internet
tempo_down_minutos = tempo_donwload / 60

print(f"O tempo aproximado de download é: {tempo_down_minutos:.2f} minutos")   