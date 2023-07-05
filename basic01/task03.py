# Task #03 作業 02【實作題】字串取代


'''
#練習：將字串當中的 not that poor 換成 good 。

❏ Requirements：

1. 輸入一個包含「not that poor 」的字串

2. 在程式中 not that poor 換成 good 後輸出

❏ Sample Input： The company is not that poor! ← 使用者輸入

❏ Sample Output： The company is good! ← 畫面輸出
'''

s = input('input a sentence with "not that poor": ') # The company is not that poor! 

if s.find('not that poor') == -1:
    print('Error input!')
else:
    s = s.replace('not that poor', 'good')
    print(s) # The company is good! 


# Task #03 作業 03【實作題】網址分割

'''
#練習：試著用 Python 將網址當中的 domain 取出來。

❏ Requirements：

1. 讓使用者可以輸入一個網址

2. 利用程式取出網址當中的 domain 後輸出

❏ Sample Input： https://www.facebook.com/dscareer ← 使用者輸入

❏ Sample Output： www.facebook.com ← 畫面輸出
'''

# method1:

s = input('please input a URL: ') # https://www.facebook.com/dscareer

s = s.split(r'//')[1].split(r'/')[0]

print(s) # www.facebook.com

# method2:

s = input('please input a URL: ') # https://www.facebook.com/dscareer

s = s.split(r'/')[2]

print(s) # www.facebook.com