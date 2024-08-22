import sys

def filtrar_por_palavra_chave(frases, palavra_chave):
    # Filtra as frases que contêm a palavra-chave
    frases_filtradas = [frase for frase in frases if palavra_chave in frase]
    return frases_filtradas

def main():
    # Lê a entrada do usuário (stdin)
    input_data = sys.stdin.read().strip()
    
    # Divide a entrada em duas partes: a lista de frases e a palavra-chave
    frases_input, palavra_chave = input_data.rsplit('\n', 1)
    
    # Converte a string de frases em uma lista, separando por vírgulas
    frases = frases_input.split(', ')
    
    # Filtra as frases que contêm a palavra-chave
    resultado = filtrar_por_palavra_chave(frases, palavra_chave)
    
    # Imprime o resultado (stdout)
    sys.stdout.write(str(resultado) + "\n")

if __name__ == "__main__":
    main()