print("Nhập vào điểm môn toán: ")
toan = int(input())
print("Nhập vào điểm môn Lý: ")
ly = int(input())
print("Nhập vào điểm Hóa: ")
hoa = int(input())
tong = toan+ly +hoa
if(tong>=15 and toan>=4 and ly>=4 and hoa>=4):
    print("Bạn đã đậu")
else:
    print("Bạn thi hỏng")