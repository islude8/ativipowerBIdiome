import sys

def normalizar_min_max(valores):
    
    x_min = min(valores)
    x_max = max(valores)
    
    
    if x_max == x_min:
        return [0.0] * len(valores)
    

    valores_normalizados = [(x - x_min) / (x_max - x_min) for x in valores]
    
 
    return valores_normalizados

def main():
   
    input_data = sys.stdin.read().strip()
    
  
    valores = list(map(float, input_data.split(',')))
    
   
    valores_normalizados = normalizar_min_max(valores)
    
   
    sys.stdout.write(str(valores_normalizados) + "\n")

if __name__ == "__main__":
    main()