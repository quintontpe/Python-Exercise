#布林資料型態(boolean)

# 正如整數屬於 int 資料型態,True 和 False 屬於布林資料型態(bool)
print('2 < 5', 2 < 5) #印出True
print('2 > 5', 2 > 5) #印出False

# 透過 bool()函式,可以將其他物件轉成布林型態
print('bool(-10)', bool(-10)) # 印出True
print('bool(0)', bool(0)) # 印出False,0是唯㇐代表False的數
print('bool(10)', bool(10)) # 印出True
print('bool("abc")', bool("abc")) # 印出True
print('bool("")', bool("")) # 印出False,空字串是唯㇐代表False的字串
