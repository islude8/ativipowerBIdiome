import sys

def remove_duplicates():
   
    input_data = sys.stdin.read().strip()
    
   
    number_list = list(map(int, input_data.split(',')))
    
  
    unique_numbers = []
    
    
    seen = set()
    
    
    for num in reversed(number_list):
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    
    unique_numbers.reverse()
    
   
    print(unique_numbers)

if __name__ == "__main__":
    remove_duplicates()