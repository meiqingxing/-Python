from distutils import filelist
#常规输出
print("hello word")
print("how are you")

#输出数值
print(520)
print(321)
print("3+1")

#将数据输出文件中；1、盘符存在；2、file=你定义的fp
fp=open('D:/text.txt','a+')  #a+的意思是，如果文件不存在就创建，如果存在就在文件后面继续追加，每执行一次就追加一次
print("hello word",file=fp)
fp.close()

#不进行换行输出
print('hello','world','python')
