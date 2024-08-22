import sys
from collections import Counter

def calcular_moda(numeros):
    
    contador = Counter(numeros)
    
    
    max_frequencia = max(contador.values())
    
    modas = [num for num, freq in contador.items() if freq == max_frequencia]
    
    
    if len(modas) == 1:
        return modas[0]
    else:
        return modas

def main():
   
    input_data = sys.stdin.read().strip()
    
  
    numeros = list(map(int, input_data.split(',')))
    
    
    resultado = calcular_moda(numeros)
    
    
    sys.stdout.write(str(resultado) + "\n")

if __name__ == "__main__":
    main()