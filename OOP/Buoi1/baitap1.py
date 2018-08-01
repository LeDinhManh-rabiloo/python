##################### Bai1
class Hocvien:
    dem = 0
    def __init__(self,name, birthday, email, phone, address, work):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.address = address
        self.work = work
        #dem = 1 attribute
        # self.dem +=1
        # Tang gia tri bien đem
        Hocvien.dem +=1
    def show_infor(self):
        print('name:',self.name)
        print('birthday:',self.birthday)
        print('email:',self.email)
        print('phone:',self.phone)
        print('Address:',self.address)
        print('Work:',self.work)
    def get_infor(self,address='Hà Nội', work='ITplus'):
        self.address = address
        self.work = work

HocvienA = Hocvien('Nguyễn Nam', '19/05/1998','namnguyen@gmail.com','01674768888','Hà Nội','TTS')
HocvienA.show_infor()
HocvienB = Hocvien('Lê An','19/05/1998','namnguyen@gmail.com','01674768888','Hà Nội','TTS')
HocvienB.get_infor()
HocvienB.show_infor()
HocvienC = Hocvien('Lê An','19/05/1998','namnguyen@gmail.com','01674768888','Hà Nội','TTS')
HocvienC.get_infor('Thái Bình','ĐH Công Nghiệp Hà Nội')
HocvienC.show_infor()
################################ bai2:
class HCN:
    def __init__(self,chieudai,chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def set(self,chieudai = 5, chieurong = 3):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def get_chieudai(self):
        return self.chieudai
    def get_chieurong(self):
        return self.chieurong
    def tinhdientich(self):
        self.dientich = self.chieudai*self.chieurong
    def chuvi(self):
        self.chuvicn = (self.chieudai+self.chieurong)*2
    def toString(self):
        infor = 'chiều dài: ',str(self.chieudai),';chiều rộng: ',str(self.chieurong),';chu vi:',str(self.chuvicn),'Diện tich: ',str(self.dientich)
        return str(infor)
    def file(self):
        self.name = input('Nhập vào tên file:')
        self.file_obj = open(self.name,'w+')
        self.info = self.toString()
        self.file_obj.write(self.info)
chunhat1 = HCN(5,4)
chunhat1.set()
chunhat1.chuvi()
chunhat1.tinhdientich()
chunhat1.chuvi()
chunhat1.toString()
chunhat1.file()

