i=0
sum=0
while i<10:
    sum+=i
    i+=1
print("Ket quả là: ",sum)
#######################Bài 2##################
n=int(input("Nhập vào số tự nhiên n: "))
i=1
gt=1
while i<=n:
    gt=gt*i
    i+=1
print("Kết quả",n,"! là:",gt)
####################################### Bài 3 ############################
a= int(input("Nhập vào số nguyên dương: "))
if a>0:
    j=1
    dem=0
    while j <= a:
        if(a%j==0):
            dem+=1
        j+=1
    if(dem>2):
        print(a,"Không là số nguyên tố")
    else:
        print(a,"Là số nguyên tố")
else:
    print("Giá trị không hợp lệ")
    a = int(input("Nhập vào số nguyên dương: "))
################################# bài 4 ################################
n= int(input("Nhập vào số n: "))
i=0
sum=0
while i<=n:
    if(i<n and i%2==0):
        sum+=i
    i+=1
print("kết quả là: ",sum)