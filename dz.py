# Задание 1
#example_str = '***---Добро пожаловать!---***'
#result = example_str.strip('* -') 
#print(result)

# Задание 2
#example_str = 'В строке, есть, ошибка, снова ошибка.'
#result = example_str.replace('ошибка', 'исправление').replace(',', '.')
#print(result)

# Задание 3
#example_str = 'Иванов;Петров;Сидоров;Кузнецов'
#result = example_str.split(';')
#print(result)
#name = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов']
#print(name[1])

# Задание 4
#words = ['Скоро', 'будет', 'контрольная']
#result = ' '.join(words) + '.'
#print(result)

# Задание 5
#nums = [4, 2, 9, 0, 4, 7] 
#list.remove(nums, 4)
#list.sort(nums)
#print(nums)

# Задание 6
#numbers = [10, 20, 30, 40]
#numbers.pop()
#print(numbers)

# Задание 7
#numbers = [5, 2, 9, 1]
#list.sort(numbers)
#print(numbers)

# Задание 8
#nums = [3, 1, 3, 7, 3, 2]
#count = nums.count(3)
#print(count) 

# Задание 9
#a = ('RGB', 255, 0, 128)
#mode, r, g, b = a
#print(mode, r, g, b)

# Задание 10
#nums = {'a': 1, 'b': 2}
#nums = dict (
#    a=1,
#    b=2,
#)
#new_dict = {'c': 3}
#nums.update(new_dict)
#nums['a'] = nums['a'] + 5
#print('Печатаем словарь с цифрами:', nums)

# Задание 11
#person = {'имя': 'Аня', 'город': 'Тверь'} 
#print(person['имя'])

# Задание 12
person = {'имя': 'Игорь'}
print(person.get('телефон', 'неизвестно'))