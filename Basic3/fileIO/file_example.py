filename = 'test_file.txt'
# create and open file
f = open(filename,'r+')#mode W+: vua kiem tra vua tao moi file
print('file has been open')
################# Read:
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


### Write:
content = 'write new content'
# f.write(content)
li = ['line 1', 'line 2']
for l in li:
    f.writelines(l)
f.close()