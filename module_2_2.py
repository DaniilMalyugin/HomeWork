# name = input('Введите ваше имя: ')
# if name == 'Urban':
#     print('Здравствуйте, администратор')
# if name == 'Daniil':
#     print('Здравствуйте, преподаватель')
# else:
#     print("Привет", name)

# number = int(input("Введите число: "))   #Fizz, Buzz, FizzBuzz
# if number % 3 == 0 or number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print('Число не подходит')

first = int(input('Ведите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')