# 生動的combo hits
# 請寫一個程式，讀入一個正整數N，先輸出一句"Fight!"
# 接著顯示生動的N combo hits。
# 所謂生動是指combo hits會以下面的方式陳列。
# Fight!
#          10 combo hits!
#         9 combo hits!
#        8 combo hits!
#       7 combo hits!
#      6 combo hits!
#     5 combo hits!
#    4 combo hits!
#   3 combo hits!
#  2 combo hits!
# 1 hit

N = int(input())
print('Flight!')
for i in range(N-1):
    print(' ' * (N-1-i) + str(N-i) + ' combo hits!')
print('1 hit')
