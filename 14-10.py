# Принимаем через input имя текстового файла, читаем его и выводим топ-10 слов в файле по количеству повторений

n = input()
f = open(n + '.txt', 'r')

top = dict()

for line in f:
    for i in line.strip().split():
        top[i] = top.get(i, 0) + 1

ans = []

for key, value in top.items():
    ans.append([value, key])


ans = sorted(ans)
num = 1

for x, y in reversed(ans[-min(10, len(ans)):]):
    print(str(num)+') ' + y)
    num += 1
