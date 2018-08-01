# def sum(a,b):
#     return a+b
# print("Nhập vào số a: ")
# a=int(input())
# print("Nhập vào số b: ")
# b=int(input())
# print("Kết quả là: ",sum(a,b))
# import time
# def timenhe():
#    localtime = time.localtime(time.time())
#    return localtime
# print(timenhe())
# def xinchao():
#     "Ham nay dung de noi hello"
#     print("hello")
# xinchao()
#Tham số bắt buộc:
def showinfor(name, mobile, email):
    print('name:',name)
    print('mobile:',mobile)
    print('email:',email)
showinfor("Manh",'0123456789','manhga3689@gmail.com')
#Tham số mặc định:
def showinfor(name, mobile, email='lemanhhvpkkq@gmail.com'):
    print('name:',name)
    print('mobile:',mobile)
    print('email:',email)
showinfor("Manh","0123456789")
#Tham số từ khóa:
#Tham số thay đổi
# def max(*var):ký hiệu bằng dấu * trc biến=> biến là list
