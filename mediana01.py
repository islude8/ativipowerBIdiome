
import sys
entrada = sys.stdin.read().strip()

numeros = list(map(float, entrada.split(',')))
def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    ponto_medio = n // 2

    if n % 2 == 0:
       
        mediana = (numeros_ordenados[ponto_medio - 1] + numeros_ordenados[ponto_medio]) / 2.0
    else:
       
        mediana = numeros_ordenados[ponto_medio]

    return mediana





sys.stdout.write(str(round(calcular_mediana(numeros), 1)))