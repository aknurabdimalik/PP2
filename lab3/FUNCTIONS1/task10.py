def unique_elements(lst):
    unique_list = [] 
    for element in lst:
        if element not in unique_list:  
            unique_list.append(element)
    return unique_list

input_string = input()
input_list = list(map(int, input_string.split()))

result = unique_elements(input_list)

print(result)
