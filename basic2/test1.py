def trungbinhcong(a,b):
    c=(a+b)/2
    return c
def guiloichao(gio):
    if(gio>=0 and gio<10):
        print("Chào buổi sáng")
    else:
        if(gio>=10 and gio<13):
            print("Chào buổi trưa")
        else:
            if(gio>=13 and gio<18):
                print("chào buổi chiều")
            else:
                print("chào buổi tối")

print("Nhập vào phần tử a: ")
a=int(input())
print("Nhap vao phan tu b: ")
b=int(input())
print("trung bình cộng là: ",trungbinhcong(a,b))
print("Mời bạn nhập giờ: ")
gio = int(input())
print("bây giờ là: ",gio)
guiloichao(gio)