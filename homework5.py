my_list = ['Яблоко', 'Банан', 'Арбуз', 'Дыня', 'Груша', 'Гранат']
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5])
my_list[2] = 'Виноград'
print(my_list)
my_dict = {my_list[0]: 'Apple', my_list[1]: 'Banana', my_list[2]: 'Grape', my_list[3]: 'Melon', my_list[4]: 'Pear', my_list[5]: 'Granate'}
print(my_dict)
print(my_dict['Яблоко'])
my_dict['Гранат'] = 'Garnet'
print(my_dict)