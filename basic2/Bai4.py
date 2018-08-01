import operator
print("nhap vao so n: ")
n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i*i
print('d=',d)

################### Bài 2################
d = {1:2,3:4,4:3,2:1,0:0}
print('Original dictionary:',d)
sorted_d = sorted(d.items(),key=operator.itemgetter(0))
print('dictionary in ascending order by value: ',sorted_d)
sorted_d = sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print('dictionary in descending order by value:',sorted_d)
############################## Bài 3 ########################
d1 = {'a':15,'b':20,'c':30,'e':60}
d2 = {'a':30,'b':20,'d':50}
d3 = d1
for key2,value2 in d2.items():
    if key2 in d1:
        d1[key2] += value2
    else:
        d1[key2] = value2
print(d1)

################################## Bai 4 #####################
d = {'IV':"S001",'V':"S002",'VI':"S001",'VII':"S005",'VIII':"S005",'IX':"S001"}
new_list = []
for key, value in d.items():
    if value in new_list:
        pass
    else:
        new_list.append(value)
print(new_list)

