'Ex1: Write a program to count positive and negative numbers in a list'
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
positive = []
negative = []
for i in data1:
    if i> 0:
        positive.append(i)
for i in data1:
    if i < 0:
        negative.append(i)
print(len(positive))
print(len(negative))

'Ex2: Given a list, extract all elements whose frequency is greater than k.'
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k = 3
tan_suat = {}
k = int(input('nhap so k:'))
for i in data2:
    if i in tan_suat:
        tan_suat[i] += 1 # là cộng vào values
    else:
        tan_suat[i] = 1
for keys,values in tan_suat.items():
        if values >= k:
            print(keys)

'''Ex3: find the strongest neighbour. Given an array of N positive integers.
The task is to find the maximum for every adjacent pair in the array.'''
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
so_lon_hon_trong_tung_cap =[]
for i in range(len(data3)-1) :
    if data3[i]< data3[i+1]:
        so_lon_hon_trong_tung_cap.append(data3[i+1])
print(so_lon_hon_trong_tung_cap)

'Ex4: print all Possible Combinations from the three Digits'
data4 = [1, 2, 3]
tap_hop_so_co_3_chu_so = []
for i in data4:
        for j in data4:
            for k in data4:
                so = 100*i + 10*j + k
                tap_hop_so_co_3_chu_so.append(so)

print(tap_hop_so_co_3_chu_so)

'''Ex5: Given two matrices (2 nested lists), the task is to write a Python program to add elements to each row from initial matrix.
For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]'''
import numpy as np
data5_list1 = [[4, 3, 5],
               [1, 2, 3],
               [3, 7, 4]]
data5_list2 = [[1, 3],
               [9, 3, 5, 7],
               [8]]
for i in range (len(data5_list1)):
    data5_list1[i].extend(data5_list2[i]) # hàm extend: đổ hết cái trong extend vào cái trước nó
    print(data5_list1[i])

'''Ex6:  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
chia_het_cho_7_va_ko_cho5=[]
for i in range (2000,3201):
    if i % 7 == 0 and i %5 != 0:
        chia_het_cho_7_va_ko_cho5.append(i)
print(chia_het_cho_7_va_ko_cho5)

'''Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.'''
def cac_chu_so_chan(a): #  ở đây a có thể là chuỗi
    for chu_so in a:
        if int(chu_so) % 2 != 0:
            return False
    return True

ket_qua= []
for i in range(1000,3001):
    chu_so = str(i)
    if cac_chu_so_chan(chu_so):
        ket_qua.append(chu_so)
print(ket_qua)

'''Ex8: Let user type 2 words in English as input. Print out the output which is the shortest chain according to the following rules:
Each word in the chain has at least 3 letters
The 2 input words from user will be used as the first and the last words of the chain 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
All the words are from the file wordsEn.txt
If there are multiple shortest chains, return any of them is sufficient'''






