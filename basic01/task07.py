#  Task #07 作業 02【實作題】n! 階乘計算
'''
#練習：n! 階乘代表 1 * 2 * 3 ... * n 的乘積總和，請用 Python 程式實現 n! 計算。

❏ Requirements：

1. 讓使用者可以自行輸入一個數字 n，請檢查 n 是否為合法數字否則回傳錯誤巡席

2. 利用程式計算 n! 的結果並且印在畫面上

❏ Sample Input #01： 4 ← 使用者輸入

❏ Sample Output #01： 24 ← 畫面輸出

❏ Sample Input #02： a ← 使用者輸入

❏ Sample Output #02： a 是一個不合法的輸入，無法運算 ← 畫面輸出
'''
x = input('please input a number: ') # 4
if not x.isdigit():
    print('x 是一個不合法的輸入, 無法運算')
else:
    x = int(x)
    total = 1
    for i in range(1,x+1):
        total = total*i
    print(total) # 24


# Task #07 作業 03【實作題】奇偶數分堆
#練習：奇偶數分堆

'''
❏ Requirements：

1. 建立一個列表（List ）初始化為 0, 1, 2... 9 的元素

2. 請利用條件判斷與迴圈將 List 中的奇數放在前面、偶數放在後面

3. 最後請將分堆後的結果印出

❏ Sample Input： [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

❏ Sample Output： [1, 3, 5, 7, 9, 0, 2, 4, 6, 8] ← 畫面輸出
'''
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
to_move = []
 

for x in L:
    if x % 2==0:
        to_move.append(x)
for i in to_move:
    L.remove(i)
    L.append(i)
#   print(i, L)


print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
