from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

n = 10

b = ''

for i in range(n):
    a = choice(lottery)
    b += str(a)
    print(b)