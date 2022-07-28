"""
Determinar a frequência das letras da língua portuguesa
utilizando um texto base
função freq(texto) --> dicionário
"""
import unidecode as uni

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
    arq = open("nove_noites.txt", "r", encoding="utf8")
    conteudo = uni.unidecode(arq.read())
    conteudo = conteudo.lower()
    print(frequencia(conteudo))
    arq.close()
    return None

if __name__ == '__main__':
    main()