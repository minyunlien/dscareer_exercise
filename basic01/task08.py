# Task #08 作業 01【實作題】階乘總和

'''
#練習：階乘總和

❏ Requirements：

1. 利用迴圈讓使用者可以重複輸入一個數字 n

2. 利用程式計算 1! + 2! + 3! + ... + n! 的總和

3. 每一個回合請將階乘總和的結果印出

❏ Sample Input： 4 ← 使用者輸入

❏ Sample Output： 33 ← 畫面輸出
'''

x = input('input a integer: ') # 4
 
sum = 0
product = 1
for i in range(1, int(x)+1):
    product *= i
    sum += product
print(sum) # 33

# Task #08 作業 02【實作題】字串計數
'''
#練習：字母頻率（frequency of letters; character frequencies），指的是各個字母在文本材料中出現的頻率。常被應用於密碼學，尤其是可破解古典密碼的頻率分析。例如，摩斯密碼中越常用的字母，其編碼符號就越短；而數據壓縮技術中也有相似的方法，如夫曼編碼就是按來源符號出現的機率大小去編碼。接下來，讓我們來試試看如何在 Python 實現從字串中計算每個字母出現頻率的問題？

❏ Requirements：

1. 讓使用者可重複輸入字串

2. 每一回合計算該字串中每個字母的出現次數並且存入 dict 中

3. 將使用者輸入字串的字母及其計數印出

❏ Sample Input： Hello World ← 使用者輸入

❏ Sample Output： {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1} ← 畫面輸出
'''

x = input('input a sentence: ') # Hello World
dic = {}
for i in x:
    if i in dic:
        dic[i]+=1
    else:
        dic[i] = 1
 
print('dic = ', dic) # {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1}