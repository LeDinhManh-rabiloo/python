# Python: cho phép tạo 1 lớp mở rộng từ 1 hoặc nhiều lớp khác
# Có đa kế thừa
# 1 đối tượng có n thuộc tính và n phương thức và các tt, pt này có thể public hoặc private
# Lớp con chỉ có thể kế thừa khi cha public
# super(): dùng để gọi đến class cha
# Trong python k có protech( chỉ sử dụng trong package)
# trong python những phương thức hoặc thuộc tính để private thì dùng 2 dấu gạch dưới: self.__name
# Đa kế thừa khai báo: class Classchilden(class1,class2,class3): ưu tiên class gần nó nhất nếu cùng phương thức
#Overwrite: cho phép lớp con có thể ghi đè các phương thức của lớp cha
# Ví dụ
class Person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    def info(self):
        print(self.name)
    def __show(self):
        print("xin chào")