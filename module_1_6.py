#Работа со словарями:
my_dict = { 'Anna': 1990, 'Vanya': 1999, 'Daniil': 1991, 'Alex': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Anna'])
print('Not existing value:', my_dict.get('Vasya', ' None'))
my_dict.update({'Roberto': 1995,
                'Kortana': 2005})
print('Deleted value:', my_dict.pop("Vanya"))
print(my_dict.items())

#Работа с множествами:
my_set = {123, 1.23, 'Kolokol', 123, 3}
print(my_set)
my_set.add(5.56)
my_set.discard(123)
print(my_set)