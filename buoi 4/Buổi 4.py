# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
from operator import index

import numpy as np
array = np.array([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
#array2= np.split(array1,26) cách này dài và lâu đc cái dùng 2 hàm đã học
#array3 = np.concatenate((array2[25],array2[24],array2[23]))
array1 =array[25::-1] #cú pháp để cắt hoặc lấy với bước nhảy, nó hơi giống for i in range(1,5,1)
#nếu không để số thì [::-1] chương trình sẽ tự hiểu bắt đầu từ đầu hoặc cuối tùy vô bước nhảy, kết thúc cũng vậy
print(array1)

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
array3 = np.array([0,10,20,40,60])
array4 = np.array([10,30,40])
phan_tu_chung =[]
for i in range(len(array3)): #cú pháp thông dụng
    for j in range(len(array4)):
        if array3[i]== array4[j]: # cũng thông dụng nốt dùng để truy cập giá trị còn nếu dùng i ==j là truy cập index
            phan_tu_chung.append(int(array3[i]))
print(phan_tu_chung)

#Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
array5= np.array([1,6,4,8,9,-4,-2,11])
max = 0
min = 0
for i in range(0,len(array5),1):
    if array5[i]> max:
        max = array5[i]
    if array5[i] < min:
        min = array5[i]
print(np.where(array5 ==max), np.where(array5 ==min))
#cách 2
a = np.max(array5)
b = np.min(array5)
print(a,b)
print(np.where(array5 ==a), np.where(array5 ==b))

'''Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
frequently and their corresponding appearance. You could ignore all punction characters such as comma, dot, semicolon, ...
Sample output:
house: 453
dog: 440
people: 312'''
