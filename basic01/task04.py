# Task #04 作業 02【實作題】元素位置異動（上）


'''
#練習：元素位置異動

❏ Requirements：

1. 建立一個列表（List ）初始化為 1, 2... 9 的元素

2. 利用程式將最右邊的元素移動到最左邊邊

2. 最後請將移動的結果印出

❏ Sample Input： [1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

❏ Sample Output： [9, 1, 2, 3, 4, 5, 6, 7, 8] ← 畫面輸出
'''

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_element = L.pop()
L.insert(0, last_element)
print(L)




# Task #04 作業 03【實作題】元素位置異動（下）

#練習：元素位置異動
'''
❏ Requirements：

1. 建立一個列表（List ）初始化為 1, 2... 9 的元素

2. 利用程式將最左邊的元素移動到最右邊

2. 最後請將移動的結果印出

❏ Sample Input： [1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化

❏ Sample Output： [2, 3, 4, 5, 6, 7, 8, 9, 1] ← 畫面輸出
'''



L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first_element = L.pop(0)
L.append(first_element)


print(L) # [2, 3, 4, 5, 6, 7, 8, 9, 1]