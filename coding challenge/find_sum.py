
def find_largest_sum(str_list):
    num_list = []
    sum_list = []
    
    for item in str_list:
        num_list = [''.join(char for char in item if char.isdigit()) for item in str_list if any(c.isdigit() for c in item)]

    for num in num_list:
        sum_list = [sum(int(char) for char in num) for num in num_list]

    return max(sum_list) 

    
print(find_largest_sum(['abcdefg123', 'dhrhdh456', '78drhrfhg9']))  # Example usage