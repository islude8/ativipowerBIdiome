import sys

def agrupar_por_faixa_etaria(idades):
   
    faixas = [
        (0, 18, '0-18'),
        (19, 35, '19-35'),
        (36, 50, '36-50'),
        (51, 70, '51-70'),
        (71, float('inf'), '71+')
    ]
    
   
    contagem_faixas = {faixa[2]: 0 for faixa in faixas}
    
  
    for idade in idades:
   
        for faixa in faixas:
            if faixa[0] <= idade <= faixa[1]:
                contagem_faixas[faixa[2]] += 1
                break  
    
    return contagem_faixas

def main():
    
    input_data = sys.stdin.read().strip()
    
    
    idades = list(map(int, input_data.split(',')))
    
 
    resultado = agrupar_por_faixa_etaria(idades)
    
   
    sys.stdout.write(str(resultado) + "\n")
    
if __name__ == "__main__":
    main()
