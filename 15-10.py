# Написать функцию, которая принимает список аргументов, выравнивание ("center" or "left" or "right"), 
# кол-во символов N, которое занимает каждый аргумент в своей строке, символ заполнения.
# Генерируем текст, где каждая строка из (длина списка аргументов) выделена под один аргумент и
# занимает N символов с выравниваением и заполнением (используем format)

def function(listA, a, n, char):
    switcher = {
        "center": "^",
        "left": "<",
        "right": ">"
    }
    arg = switcher.get(a)
    str = ""
    for i in listA:
            str += ('{0:'+ char + arg + '%s'%n + 's}').format(i)
            str += '\n'
    return str

print(function(['AAA','SSSSS','G'], 'center', 10, '!'))
