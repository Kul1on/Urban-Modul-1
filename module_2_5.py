def get_matrix(n, m, value):
    matrix = []  # Initialize an empty list to store rows
    
    for _ in range(n):  
        row = []  
        for _ in range(m):  
            row.append(value)  
        matrix.append(row)  
    
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)


print(result1)
print(result2)
print(result3)
