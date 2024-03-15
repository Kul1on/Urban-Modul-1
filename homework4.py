immutable_var = (21, 'Вячеслав', True)
print(immutable_var)
# immutable_var[0] = 22  # Изменять элементы кортежа нельзя, он неизменяемый
# print(immutable_var)

mutable_list = (['Банан', 'Ананас', 'Апельсин', 'Огурец', 'Мандарин'], 21, 'Груша', False)
mutable_list[0][3] = 'Клементин'
print(mutable_list)
