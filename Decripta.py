"""
Descriptografar texto
função decripta(texto, desloc) --> texto original
pegando apenas letras de a-z
exemplo:
texto: Spá, xyhs fiq?
deslocamento: 4
resultado: Olá, tudo bem?
"""
def decripta(texto, desloc):
    orig = ""
    for i in range(len(texto)):
        if (ord(texto[i]) not in range(65, 91)) and (ord(texto[i]) not in range(97, 123)):
            orig += texto[i]
        else:
            aux = ord(texto[i])
            aux -= desloc
            if aux <= 64:
                aux += 26
            elif aux >= 91 and aux <= 96:
                aux += 26
            orig += chr(aux)
    return orig

def main():
    texto = input("Digite o texto a ser descriptografado: ")
    desloc = int(input("Digite o deslocamento: "))
    print("Resultado:", decripta(texto, desloc))
    return None

main()
