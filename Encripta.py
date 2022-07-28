"""
cifra de césar
fução encripta(texto, desloc) --> texto criptografado
pegando apenas letras de a-z
exemplo:
texto: Olá, tudo bem?
deslocamento: 4
resultado: Spá, xyhs fiq?
"""
def encripta(texto, desloc):
    cript = ""
    for i in range(len(texto)):
        if (ord(texto[i]) not in range(65, 91)) and (ord(texto[i]) not in range(97, 123)):
            cript += texto[i]
        else:
            aux = ord(texto[i])
            aux += desloc
            if aux > 91 and aux < 97:
                aux -= 26
            elif aux > 123:
                aux -= 26
            cript += chr(aux)
    return cript

def main():
    texto = input("Digite o texto a ser criptografado: ")
    desloc = int(input("Digite o deslocamento: "))
    print("Resultado:", encripta(texto, desloc))
    return None

main()
