def calculate_structure_sum(data):
    total = 0

    for item in data:
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, list):
            total += calculate_structure_sum(item)
        elif isinstance(item, dict):
            total += calculate_structure_sum(item.keys())
            total += calculate_structure_sum(item.values())
        elif isinstance(item, tuple):
            total += calculate_structure_sum(item)
    
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result) 
