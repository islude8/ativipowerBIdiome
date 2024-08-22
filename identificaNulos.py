import sys

def count_nones():
  
    input_data = sys.stdin.read().strip()
    
    
    input_data = input_data.replace('None', ',None,')
    

    values = []
    for item in input_data.split(','):
        item = item.strip()
        if item == "None":
            values.append(None)
        elif item.isdigit():
            values.append(int(item))
        elif item == "":
            continue 

   
    none_count = values.count(None)
    
    
    print(none_count)

if __name__ == "__main__":
    count_nones()




