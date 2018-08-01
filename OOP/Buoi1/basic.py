#Tính chất: Trừu tượng, đóng gói , kế thừa và đa hình
# Cú pháp khai báo:
#                     class Tên Class:
#                         Mô tả
################ Lưu đồ:
#
#
# Begin--------->Định nghĩa đối tượng(class, khai báo thuộc tính, phương thức)-------->Khởi tạo instance của đối tượng--->Từ instance đã có
# (gọi đến thuoc tính, pt của đt)---->end
##################################### Ví dụ
# class Animal:
#      def get_name(self,name):
#          self.name = name
#          pass

# class Sinhvien:
#     'Oject sinh vien'
#
# class Nhanvien:
#     'Oject nhan vien'
class Person:
    def __init__(self, name, age, mobile):#phương thức khởi tạo
        self.name = name
        self.age = age
        self.mobile = mobile
    def get_person(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Mobile:',self.mobile)

student = Person('Ricky','18','0927276868')
print(student.name)
student.get_person()
#### chú ý:
# Hàm khởi tạo ___init___ có 2 tham số là bắt buộc và mặc định thì ts bắt buộc phải trcs mặc định,
# trong 1 classs chỉ có 1 hàm khởi tạo
class Nhanvien:
    dem = 0#bien toan cục
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Nhanvien.dem +=1
    def hien_thi_so_luong(self):
        print("Tỏng số nhân viên là: %d" %Nhanvien.dem)
    def hienthinhanvien(self):
        print('Tên:', self.name, ',lương: ',self.salary)
dev = Nhanvien('Nguyen Nam','10000000000$')
pm = Nhanvien('Hoai nam','100000000$')
dev.hien_thi_so_luong()
dev.hienthinhanvien()
pm.hienthinhanvien()
# Lấy giá trị bằng getattr(đối tượng, thuộc tính,default)
print(getattr(dev,'name'))
#### Check xem có thuộc tính đó hay k: hassattr(đối tượng, thuộc tính)
#### Set giá trị cho thuộc tính dùng: setattr(đối tượng, thuộc tính,, giá trị)
