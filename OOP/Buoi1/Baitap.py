############################## Bai 4 OOP.pdf
class Account:
    def __init__(self,sotaikhoan,tenchutaikhoan,sotientrongtk):
        self.sotaikhoan = sotaikhoan
        self.tenchutaikhoan = tenchutaikhoan
        self.sotientrongtk = sotientrongtk
    def getsotaikhoan(self):
        return self.sotaikhoan
    def setsotaikhoan(self,sotaikhoan):
        self.sotaikhoan = sotaikhoan
    def gettenchutaikhoan(self):
        return self.tenchutaikhoan
    def settenchutaikhoan(self,tenchutaikhoan):
        self.tenchutaikhoan =tenchutaikhoan
    def getsotientrongtk(self):
        return self.sotientrongtk
    def setsotientrongtk(self,sotientrongtk):
        self.sotientrongtk = sotientrongtk
    def TotString(self):
        infor = "số tài khoản: ",str(self.sotaikhoan),"Chủ tài khoản: ",str(self.tenchutaikhoan),"Số tiền trong tài khoản: ",str(self.sotientrongtk)
        return infor
    laisuat = 0.035
    def __contructor(self,sotaikhoan, tenchutaikhoan, sotientrongtk = 50 ):
        self.sotaikhoan = sotaikhoan
        self.tenchutaikhoan = tenchutaikhoan
        self.sotientrongtk = sotientrongtk
    def naptien(self,sotiennap):
        self.sotientrongtk = self.sotientrongtk + sotiennap
        return self.sotientrongtk
    def Ruttien(self,sotienrut):
        if self.sotientrongtk <= (sotienrut+0.33):
            print("Số tiền trong tài khoản không đủ để thực hiên giao dich")
        else:
            self.sotientrongtk = self.sotientrongtk - (sotienrut + 0.33)
            print("So tien da rut: ",sotienrut)
            print("So tien con lai: ", self.sotientrongtk)
            return self.sotientrongtk
    def Daohan(self):
        self.sotientrongtk = self.sotientrongtk + (self.sotientrongtk * Account.laisuat)
        print("số tiền còn lại: ",self.sotientrongtk)
        return self.sotientrongtk
    def chuyentien(self,tentknhan,sotien):
        if(self.sotientrongtk <= sotien ):
            print("Số tiền trong tài khoản không đủ để thực hiện giao dịch này")
        else:
            print("bạn đã chuyển cho",tentknhan.tenchutaikhoan," so tien: ",sotien)
            tentknhan.naptien(sotien)
            self.Ruttien(sotien)


A = Account("123456789","A",50000)
B = Account("123456789","B",50000)
A.setsotaikhoan('12345678910')
A.getsotaikhoan()
A.settenchutaikhoan("A")
A.gettenchutaikhoan()
A.setsotientrongtk(500000000)
A.getsotientrongtk()
A.naptien(5000000)
A.Ruttien(550000)
A.Daohan()
A.chuyentien(B,500000)
B.Daohan()
print(B.TotString())

#################################### Bài 7