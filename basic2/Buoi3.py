######################### Vòng lặp white
# a=int(input("Nhập vào số a: "))
# i=0
# sum =0
# while i<a:
#     sum+=i
#     i+=1
#     continue#chạy quay lại đầu
#     print("xin chào")
# else:
#     print("đã thoát vòng lặp")
# print("Tổng là: ",sum)
############################## Kiểu dữ liệu string và list và dictionnary
####### Kiểu chuỗi
# x= "Xin chào 'Nam'"
# print(x[2:8])
# print(x[2:])
# print(x[:8])
# x1="Hello"
# x2="world"
# x3="He"
# print(x1+x2)
# print(x1*3)
# print(x3 in x1)#Kiểm tra 1 đoạn text có chứa hay k
# print(x1.capitalize())
# print(str.capitalize(x2))
# print(len(x1))
####### Kiểu list
# list là kiểu duwxx liệu thay đổi
# sublist =['seven',8,9]
# L = [1,"two",3,"four","five",6, sublist]
# print(L[6])
# print(len(L))
# for i in L:
#     print(i)
# list = [1998,1999,2000,2001,2002,2003]
# print(list)
# list[1]=1996
# print(list)
# #Thêm 1 pt vào cuối day dùng append
# list.append(30)
# print(list)
# # thêm vào vị trì nào đó dùng insert
# list.insert(1,1995)
# print(list)
# del list[7] # Xoa theo index
# print(list)
# list.remove(1995)
# print(list)
# list.reverse()
# print(list)
######## Kiểu dữ liệu Tuple
# Là đối tượng bất biến
# tuple1= (1,2,3,4,5,5,6,7,8,9)
# list1 = list(tuple1)
# print(list1)
# print(tuple1)
# print(tuple1.index(5))# xác định chỉ số nhỏ nhất của pt
############################################## Dictionary#################
# Là kiểu dữ liệu từ điển
# Khai báo:
#d ={'name':'Nguyễn Văn A'} hoặc d = dict()
# {key1:value1,key2:value2,key3:value3}
#key là kiểu dữ liệu bất biến
# t=(1,2,3)
# l=[2,4,6]
# d = dict()
# d['key']='value'
# d['key2']='value2'
d1 = {'name':'Nguyễn Văn A','Age':19}
# print('d1:',d1,d)
#dùng for với 2 biến chạy để lấy dữ liệu và hàm .items()
# for key,value in d.items():
#     print('Key:',key,'-Value:',value)
# print(d['key'])
# có thể sử dụng hàm update: d.update(): dùng cho cả thêm mới và sửa
d1['name']='Lê Đình Mạnh'
d1['mobile']='0123456789'
print(d1)
d1.update({'mobile':'01235678968','email':'manhga3689@gmail.com'})
print(d1)
del d1['mobile']
print(d1)
d1.__delitem__('email')
print(d1)
print(d1.keys())
print(d1.values())
d = {'1':'a','2':'b','3':'c'}
# sorted(d.items(),key = operator.itemgetter(0))