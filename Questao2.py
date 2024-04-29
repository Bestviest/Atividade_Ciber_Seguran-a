def cifra_feistel(texto_binario, rodadas):
    def funcao_F(bloco, chave):
        return ''.join(str(int(b) & int(k)) for b, k in zip(bloco, chave))

    def deslocamento_circular_esquerda(bloco):
        return bloco[1:] + bloco[0]

    L, R = texto_binario[:len(texto_binario)//2], texto_binario[len(texto_binario)//2:]
    for _ in range(rodadas):
        L, R = R, ''.join(str(int(l) ^ int(r)) for l, r in zip(L, funcao_F(R, L)))
        L = deslocamento_circular_esquerda(L)
    return L + R

print(cifra_feistel("01101100", 2))