
def find_largest_sum(str_list):
    num_list = []
    sum_list = []
    
    for item in str_list:
        num_string = ''
        for char in item:
            if char.isdigit():
                num_string += char
        if num_string:
            num_list.append(num_string)

    for num in num_list:
        sum = 0
        for char in num:
            sum += int(char)
        sum_list.append(sum)

    return max(sum_list) 

    
print(find_largest_sum(['abcdefg123', 'dhrhdh456', '78drhrfhg9']))  # Example usage