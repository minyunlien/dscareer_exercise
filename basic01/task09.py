# Task #09 作業 02【實作題】定義函式
'''
#練習：定義一個計算質數的函數。

❏ Requirements：

1. 讓使用者輸入一個整數 n

2. 請分別定義兩個 Function: isPrime(n) 回傳 n 是否為質數、primes(n) 回傳小於 n 質數

❏ Sample Input： 20 ← 使用者輸入

❏ Sample Output： 2, 3, 5, 7, 11, 13, 17, 19 ← 畫面輸出
'''

x = input('please input a positive integer: ')

x = int(x)

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
    return True

# # 回傳小於 n 質數

def primes(x):
    prime_list = []
    for j in range(1, x):
        if isPrime(j) == True:
            prime_list.append(j)
    return prime_list
    
print(isPrime(x))

print(primes(x))

# Task #09 作業 03【實作題】計算總和的函數
'''
#練習：請撰寫一個 sum(…) function 將輸入的參數計算總和後回傳。

❏ Requirements：

1. 定義一個可以計算總和的 sum function，其中參數的數量可以是動態不固定的

❏ Sample Input #01： f(1, 2, 3) ← 預設呼叫

❏ Sample Output #01： 6 ← 畫面輸出

❏ Sample Input #02： f(1, 2, 3, 4, 5) ← 預設呼叫

❏ Sample Output #02： 15 ← 畫面輸出
'''

def f_sum(*kwargs):
    total = 0
    for x in kwargs:
        total+=x
    return total

print(f_sum(1, 2, 3, 4, 5))