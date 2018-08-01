##################### Bài 1
# file_name = "hello.txt"
# # f = open(file_name,'w+')
# r = open(file_name,'r+')
# print(r.read())
# ################### Bài 2
# print('Nhập vào số n: ')
# n= int(input())
# filename = 'h.txt'
# f = open(filename,'r+')
# for i in range(n):
#     print(f.readlines())
# ################# Bài 3
# filen = 'doanvan.txt'
# d = open(filen,'r+')
# m = ['xin chao cac ban','hello']
# for l in m:
#     d.writelines(l)
# print(d.read())
####################### Bai 1
# file_name = 'demso.txt'
# n= int(input("Nhập vào số n: "))
# def taotep(file_name,n):
#     f = open(file_name,'w+')
#     s= []
#     for i in range(n):
#         s[i] = int(input('Nhập số: '))
#     for l in s:
#         f.writelines(l)
#     f.close()
# def doctep(file_name):
#     r = open(file_name,'r+')
#     s =r.read()
#     n = list(s)
#     dem = len(n)
#     sdu = 0
#     lonnhat = max(n)
#     nhonhat = min(n)
#     for i in n:
#         m = int(i)
#         if m>0:
#            sdu+=1
#     print(dem)
#     print(sdu)
#     print(lonnhat)
#     print(nhonhat)
#     r.close()
# taotep(file_name,n)
# doctep(file_name)
# n = input('Nhập vào các số nguyên: ')
f = open('Cau1.txt','r+')
# input_list = n.split(',')
# f.write(n)
# print("Số lượng phần tử: ",len(input_list))

########################## Bai 2
# file = 'Sv.txt'
# def tao():
#     r = open(file,'w+')
#     x = int(input("Nhập vào số x"))
#     _list = []
#     for i in range(x):
#         _list[i] = input()
#     for l in _list:
#         r.writelines(l)
#     r.close()
# def doc():
#     r = open(file,'r+')
#     _list = r.readline()
#     for i in _







