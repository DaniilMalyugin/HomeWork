#Задайте переменные разных типов данных:
immutable_var = (1, 2, 3, 'c,a,b')
print(immutable_var)

#Изменение значений переменных: почему нельзя изменить значения элементов кортежа.
#immutable_var [0] = 2
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
#Кортеж - нельзя изменять после создания

mutable_list = [1, 2, 3, 'c', 'a', 'b']
mutable_list[0] = 3
mutable_list[1] = 2
mutable_list[2] = 1
mutable_list[3] = 'a'
mutable_list[4] = 'b'
mutable_list[5] = 'c'
print(mutable_list)