#File : Tệp, tập tin,...
#python làm việc chủ yếu với file hình ảnh và văn bản
#Quy trình làm việc với file: Tạo file -> Mở file-> Đọc file và ghi file->đóng file -> kết thúc
############################### Cú pháp:
# file = open(tên file,kiểu truy cập, buffering: bộ nhớ đệm để nhớ file đó)
#kiểu truy cập: r: mở file chỉ đọc
#               r+:
# filename = 'test_file.txt'
###### create and open file
# f = open(filename,'w+')#mode W+: vua kiem tra vua tao moi file
# print('file has bên open')
########## Readfile:
# content = f.read(so luong kt can doc)
# content = f.read()
# print('file content:',str(content))
# s1 = f.readline()
# s2 = f.readline()
# s3 = f.readline()
# s4 = f.readline()
# def del_empty(string):
#     new_s = string.replace('\n','')
#     return new_s.replace('\n','')
# print(s1,s2.replace('\n',''),s3.replace('\n',''))

################ Write:
# content = 'write new content'
# f.write(content)
#f.seek(0): đưa con trỏ về đầu file
 # _file = open('cau2.txt','r+')
 # _list = _file.readline()
 # Hàm sorted dùng sắp xếp 1 list phần tử là 1 dict
