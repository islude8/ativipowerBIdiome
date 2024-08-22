import sys
print('Insira os dados')
input_data = sys.stdin.readline().strip()


if input_data:
    try:
        
        numbers = [float(num) for num in input_data.split(',')]

        
        total_sum = sum(numbers)

      
        quantity = len(numbers)

     
        average = total_sum / quantity

       
        print("A média é: ")
        sys.stdout.write(str(round(average, 1)))
    except ValueError:
        print("Entrada inválida! Certifique-se de que todos os valores sejam números separados por vírgula.")
else:
    print("Nenhum dado foi fornecido.")