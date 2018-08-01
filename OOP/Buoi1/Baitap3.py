class Person:
    def __init__(self,name,add):
        self.name = name
        self.address = add
    def set_name(self,name):
        self.name = name
    def set_address(self,add):
        self.address = add
    def info(self):
        a = 'Name: ',self.name,' Address: ',self.address
class Student(Person):
    def __init__(self,name,add,mark_one,mark_tow):
        super().__init__(name,add)
        self.mark_one = mark_one
        self.mark_tow = mark_tow
    def set_mark(self,m_one):
        self.mark_one = m_one
    def set_mark(self,m_tow):
        self.mark_tow = m_tow
    def mark_sum(self):
        return self.mark_one + self.mark_tow
class Employee(Person):
    def __init__(self,name,add,salary,title):
        super().__init__(name,add)
        self.salary = salary
        self.title = title
    def set_salary(self,salary):
        self.salary = salary
    def set_title(self,title):
        self.title = title
    def _info(self):
        s = self.info(),' '
class Curtomer(Person):
    def __init__(self,name,add,mode,invoice):
        super().__init__(name,add)
        self.mode = mode
        self.invoice = invoice
    def set_mode(self,mode):
        self.mode = mode
    def set_invoice(self,invoice):
        self.invoice = invoice
    def _info(self):
        s = self.info(),' Loai xe ban: ',self.mode,' Ma hoa don: ',self.invoice
        return s



n = int(input('Lựa chọn kiểu đối tượng: '))
name = input('Nhập vào tên: ')
add = input('Nhập vào địa chỉ: ')
if n ==0:
    m_one = float(input('Nhập vào điểm môn 1: '))
    m_tow = float(input('Nhập vào điểm môn 2: '))
    stu = Student(name,add,m_one,m_tow)
    print()

