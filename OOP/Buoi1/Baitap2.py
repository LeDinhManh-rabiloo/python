class student():
    def __init__(self,student_code,name,age):
        self.student_code = student_code
        self.name = name
        self.age = age
    def _student_info(self):
        a = 'Mã sinh viên: ',str(self.student_code),' Tên: ',str(self.name),' Tuổi: ',str(self.age)
class InternalStudent(student):
    def __init__(self,student_code,name,age):
        student.__init__(student,student_code,name,age)
    def set_student_type(self,year):
        s = ''
        if year ==2:
            s = 'Trung cấp'
        else:
            if year == 3:
                s = 'Cao Đẳng'
            else:
                if year == 4:
                    s = 'Đại học'
                else:
                    s = ''
        return s
    def student_info(self):
        a = student._student_info(),' Type: ',self.s
class GlobalStudent(student):
    def __init__(self,student_code,name,age,country):
        student.__init__(student,student_code,name,age)
        self.country = country
n = int(input('Nhập loại sinh viên: ')) # Nếu n == 1 sinh viên trong nc, nếu n == 0 sv liên kết
id = input('Nhập mã sinh viên: ')
name = input('Tên sinh viên: ')
age = input('Nhập tuổi sv')
if n == 1:
    year = int(input('Nhập số năm học: '))
    ist = InternalStudent(id,name,age)
    ist.set_student_type(type)
    print(ist.student_info(year))
