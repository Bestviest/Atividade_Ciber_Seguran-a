def decifra_cesar(texto_cifrado, chave):
    texto_decifrado = ""
    for c in texto_cifrado:
        if c.isalpha():
            ascii_offset = ord('a') if c.islower() else ord('A')
            c_index = ord(c) - ascii_offset
            novo_c_index = (c_index - chave) % 26
            novo_c = chr(novo_c_index + ascii_offset)
            texto_decifrado += novo_c
        else:
            texto_decifrado += c
    return texto_decifrado

texto_cifrado = "Kjqne fvzjqj vzj ywfsxkjwj t vzjxfgj j fuwjsij t vzj jsxnsf.Htwf Htwfqnsf."
for chave in range(26):
    print(f"Chave={chave}, Texto={decifra_cesar(texto_cifrado, chave)}")