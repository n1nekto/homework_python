from datetime import datetime

def kunkka(text, year, month, day):
    date = datetime(year, month, day)
    f = open('journal.txt', 'a')
    f.write(str(date)[:-9] + ' '+ text + '\n')
    f.close()
print()

kunkka('my last message...', 1777, 10, 8)