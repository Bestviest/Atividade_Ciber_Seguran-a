s1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 9, 3, 10, 5, 0],
    [14, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 3, 10, 0, 6, 13]
]

entrada = "011010"

# Dividir a entrada em blocos de 3 bits
blocos = [entrada[i:i+3] for i in range(0, len(entrada), 3)]

# Realizar a substituição para cada bloco
saida = []
for bloco in blocos:
    # Converter o bloco de binário para decimal
    linha = int(bloco[0], 2)
    coluna = int(bloco[1:], 2)
    
    # Usar os valores decimais para indexar a caixa S1
    substituicao = s1[linha][coluna]
    
    # Converter a substituição de volta para binário e adicionar à saída
    saida.append(bin(substituicao)[2:].zfill(3))

# Juntar os blocos de saída para formar a saída final
saida_final = "".join(saida)

print("Saída:", saida_final)