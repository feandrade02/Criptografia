"""
cifra de césar
fução encripta(texto(str), desloc(str)) --> texto criptografado(int)
pegando apenas letras de a-z
exemplo:
texto: Olá, tudo bem?
deslocamento: 4
resultado: Spá, xyhs fiq?
"""
import unidecode as uni

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
    #texto = input("Digite o texto a ser criptografado: ")
    arq = open("Hino_nacional.txt", "r", encoding="utf8")
    texto = uni.unidecode(arq.read())
    texto = texto.lower()
    desloc = int(input("Digite o deslocamento: "))
    #print("Resultado:", encripta(texto, desloc))
    res = open("Hino_nacional_codificado.txt", "w")
    res.write(encripta(texto, desloc))
    arq.close()
    res.close()
    return None

if __name__ == '__main__':
    main()
