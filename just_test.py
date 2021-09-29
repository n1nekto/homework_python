# a = list()
# b = tuple()
# c = dict()
# d = set()
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

for i in range(0,50):
	print(i, end=',')

for i in range(0,50,2):
	print(i, end=',')


first_while = 0
while first_while < 51:
	print(first_while, end=' ')
	first_while += 1
print('')

second_while = 0
while second_while < 51:
	print(second_while, end=' ')
	second_while += 2
