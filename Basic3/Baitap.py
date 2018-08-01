#### Bai 1#####
pi = 3.14
def dientich(dai,rong):
    "Ham tinh dien tich hcn"
    s= dai*rong
    return s
def dientichtron(r):
    "Ham tinh dien tichhinh tron"
    shtron = pi* pow(r,2)
    return shtron
def danhsachchiahet3(list):
    "Ham dua ra mang chia het cho 3"
    outlist =[]
    for i in list:
        if i%3==0:
            outlist.append(i)
    return outlist
###### Tong hop ###
print("Nhap vao chieu dai: ")
dai = int(input())
rong = int(input("Nhap vao chieu rong: "))
print(dientich(dai,rong))
r= int(input("Nhap vao ban kinh: "))
print(dientichtron(r))
list = [1,3,8,9,10,15]
print(danhsachchiahet3(list))

