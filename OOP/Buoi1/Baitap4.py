class Person():
    def __init__(self,name,birthday,cmnd):
        self.name = name
        self.birthday = birthday
        self.cmnd = cmnd

class Hotel(Person):
    def __init__(self,name,birthday,cmnd,ngaytro,price):
        super().__init__(name,birthday,cmnd)
        self.ngaytro = ngaytro
        self.price = price
    def set_cmnd(self,cmnd):
        self.cmnd = cmnd
    def del_cmnd(self,cmnd):
        self.cmnd = None
    def show_cmnd(self,cmnd):
        print('Số cmnd: ',self.cmnd)
n = int(input('Nhập số lượng khách'))
list_customer = []
for i in range(1,n+1):
    print('Thông tin khách hàng thứ: ',i,': ')
    list_customer = []
    cmnd = input('số cmnd: ')
    name = input('Họ và tên: ')
    birthday = input('Ngày sinh: ')
    date = input('Số ngày thuê: ')
