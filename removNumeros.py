import sys

def remove_duplicates():
   
    input_data = sys.stdin.read().strip()
    

    number_list = list(map(int, input_data.split(',')))
    
    
    unique_numbers = list(set(number_list))
    
    
    print(unique_numbers)

if __name__ == "__main__":
    remove_duplicates()