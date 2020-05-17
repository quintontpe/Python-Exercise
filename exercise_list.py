##############################
## LIST 產生器(Generators)

a = [0 for i in range(5)]
print(a)

print('-' * 80)

##############################
## a sqr list from 0 to 4
n = 5
a = [i ** 2 for i in range(n)]
print(a)
print('-' * 80)

##############################
# 產生包含100個亂數(介於1到9)的串列

from random import randrange
n = 100
a = [randrange(1, 10) for i in range(n)]
print(a)

print('-' * 80)
##############################
# 切片(Slices)
A = [1, 2, 3, 4, 5, 6, 7]
print(A)
A[::-2] = [10, 20, 30, 40]
print(A)
print('-' * 80)
##############################
