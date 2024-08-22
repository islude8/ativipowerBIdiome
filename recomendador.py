import sys

print("EscrevaNessabagaça: ")
consumo_mensal = sys.stdin.read()

def recomendar_plano(consumo_mensal):
    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif 10 < consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"


    
    
sys.stdout.write(recomendar_plano)