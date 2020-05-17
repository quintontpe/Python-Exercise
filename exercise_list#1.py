##############################
a = [[1, 2, 3], [4, 5, 6]]
print('a[0]:', a[0])
print('a[1]:', a[1])
b = a[0]
print('b   :', b)
print('a[0][2]:', a[0][2])
a[0][1] = 7
print('a:', len(a), a)
print('b:', len(b), b)
b[2] = 9
print('a[0]:', a[0])
print('b   :', b)
print('-' * 80)

##############################
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print('-' * 80)

##############################
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    print(row)
    for elem in row:
        print(elem, end=' ')
    print()
print('-' * 80)
a=[[0] * 3] * 2  # wrong solution
print(a)
a[1][1] = 3
print(a)

print('-' * 80)

##############################
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
print(a)
a[1][1] = 3
print(a)
print('-' * 80)

##############################
n = 3
m = 2
a = []
for i in range(n):
    a.append([1] * m)
    a.append([5] * m)
print(a)
a[1][1] = 3
print(a)
print('-' * 80)

##############################
n = 3
m = 4
a = [[0] * m for i in range(n)]
print(a)
a[1][1] = 3
print(a)
print('-' * 80)

##############################
s = 'ab12c59p7dq'

digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)

alphabet = []
for symbol in s:
    if 'abcdefg'.find(symbol) != -1:
        alphabet.append(symbol)
print('[' + ', '.join([str(i) for i in alphabet]) + ']')
print('-' * 80)

##############################

print('input a number N')
a = int(input())
num=0
s = []
for i in range(a):
    s.append(i+num)
    num = s[i]
print(', '.join([str(x) for x in s])) 

print('-' * 80)

##############################

print('Snakify: List exercise: Queens')
print('Input 8 pairs in 8 lines:')
t = [0,0]
q = []    #  [ [x,y], [x,y], ...]
for i in range(8):
    #t=input().split()
    #print('t', t)
    q.append([int(s) for s in input().split()])
    print('q['+ str(i) + ']', q[i])

result = 'NO'
for i in range(len(q)-1):
    print(i)
    for j in range(i+1, len(q)):
        #print('i=', i, 'j=', j)
        x = abs(q[i][0] - q[j][0])
        y = abs(q[i][1] - q[j][1])
        if x == 0 or y == 0:
            result = 'YES'
            print(i, q[i], '-', j, q[j], 'YES')
            #break
        elif x == y:
            result = 'YES'
            print(i, q[i], '-', j, q[j], 'YES')
            #break
        else:
            print(i, q[i], '-', j, q[j], 'NO')            
print(result)
print('-' * 80)

#############################
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        print(i, j)
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
            print('     YES')

if correct:
    print('NO')
else:
    print('YES')

print('-' * 80)

