"""
Função decodifica(texto(str), frequência(dict)) --> texto original(str)
Recebe o texto criptografado e a frequência de cada letra da língua portuguesa
Assim, determina a letra de maior frequência do texto e compara com a letra a, que é a de maior frequência da língua portuguesa.
Dessa forma, encontra a distância entre elas, que será o deslocamento procurado.
depois chamar a função decripta que devolve o texto original.
"""
import unidecode as uni

def decodifica(texto, freq):
    maiorfreq = 'a'
    maiorfreqtxt = 'a'
    
    for chave in freq:
        if freq[maiorfreq] < freq[chave]:
            maiorfreq = chave

    freqtexto = frequencia(texto)
    for chave in freq:
        if(freqtexto[maiorfreqtxt] < freqtexto[chave]): 
            maiorfreqtxt = chave

    desloc = ord(maiorfreqtxt) - ord(maiorfreq)

    orig = decripta(texto, desloc)
    return orig

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

def frequencia(texto):
    letras = "abcdefghijklmnopqrstuvwxyz"
    dicio = dict()
    dicio = dicio.fromkeys(letras, 0)
    tam = 0

    for chave in dicio:
        for i in texto:
            if i == chave:
                dicio[chave] += 1
                tam += 1
    
    for chave in dicio:
        dicio[chave] /= tam
  

    return dicio

def main():
    #texto = input("Digite o texto a ser descriptografado: ")
    texto = open("Hino_nacional_codificado.txt", "r", encoding="utf8")
    texto2 = texto.read()
    arq = open("nove_noites.txt", "r", encoding="utf8")
    conteudo = uni.unidecode(arq.read())
    conteudo = conteudo.lower()
    freq = frequencia(conteudo)
    #print("Resultado:", decodifica(texto, freq))
    res = open("Hino_nacional_decodificado.txt", "w")
    res.write(decodifica(texto2, freq))
    arq.close()
    texto.close()
    res.close()
    return None

if __name__ == '__main__':
    main()