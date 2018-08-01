################################# Bai 1################
list = [1,2,3,4,5,6,7,8,9]
tong = 0
for i in list:
    tong+=i
print("Tong la: ",tong)
################################ Bai 2 ###################
_list = [1,2,3,4,5]
tich = 1
for i in _list:
    tich = tich*i
print("tich cua day la: ",tich)

################################ Bai 3 ####################
list2 = [1,2,3,4,5,6,7,8,9]
listx = []#even
listl = []#odd
for i in list2:
    if(i%2==0):
        listx.append(i)
    else:
        listl.append(i)
print("list chan la: ",listx)
print("list le la: ", listl)

############################### Bai 4 #######################
_list2 = ['red','green','white','black','pink','yellow']
_newlist = _list2[2:4]
print("danh sach moi la: ",_newlist)
###################################### Bai 5 ##################
_list3 = ['zero','three']
_list4 =['one','two']
_list3.insert(1,'one')
_list3.insert(2,'two')
_new = _list3
print("danh sach new la: ",_new)

########################################## Bai 6 #######################
List = ['abc','xyz','aba','1221','ii','ii2','5yhy5']
dem =0
j=0
for i in List:
    print(i)
    a= len(i)
    if(i[0]==i[a-1]):
        dem+=1
print("số dãy thoa mãn là: ",dem)
####################################### Bài 7 #########################
_List = ['abc','xyz','abc','1221','ii','12','5a']
_newlist2 = []
for i in _List:
    if _List.count(i):
        _newlist2.append(i)

print("Danh sách mới: ",_newlist2)


