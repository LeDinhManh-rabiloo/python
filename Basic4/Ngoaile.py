# exception: Ngoai le dung de xu ly cac trg hop bat thuong xay ra
try:#Bat ngoai le
    a = 10
    b= 2
    print(a/b)
    b+=3
    print(a/b)
    b=0
    print(a/b)
except Exception as ex:#nem ngoai le
    print('Err:',ex)#in ra loi
    print('finish')
a = 10
b = 20
c = None
def example(x,y):
    try:
        return y/x
    except Exception as ex:
        print('Err:',ex)
    finally:#tiep tuc thuc hien cac cau lenh phia sau du ham da tra ve gt hay chua
        c = 2
        print('Finish function', c)
example(2,10)