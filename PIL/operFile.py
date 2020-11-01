import time

# # 读取文件
# # 只读模式
# try:
#     f = open(r"D:\temp.txt", mode='r')
#     # # buffer 缓冲区
#     # ch = f.read(1024)
#     # print(ch)
#     ch = f.readline()
#     ch = f.readline()
#     print(ch)
# except:
#     print("error")
# finally:
#     # 关闭文件流
#     f.close()

# f = open(r"D:\temp.txt", mode='r')
# # while True:
# #     ch = f.readline()
# #     print(ch)
# #     if ch is "":
# #         break
# line = f.readline()
# while line is not "":
#     print(line)
#     line = f.readline()

# 一次性的读取全部数据 并且返回一个list
# print(f.readlines())
# f.close()

# 循环迭代f对象
# for e in f:
#     print(e)
# # f.close()
#
#
# f.write("d")
#

# 126 ASCII码

# f = open("temp.txt",'w',encoding='utf-8')
# # f.write("你好吗?\n")
# # f.write("我很好")
#
# f.write("""你好吗？
# 我很好""")
#
# # 异步IO 同步IO
#
# # 暂停10秒
# time.sleep(10)
#
# # 清空缓存
# f.flush()# 把缓存的数据写入硬盘
#
# f.close()
#
# f = open("temp.txt","a",encoding="UTF-8")
# f.write("你在哪里?")
# f.flush()
# f.close()

# 读写模式
# f = open("temp.txt","r+",encoding="UTF-8")
#
# f.write("hello")
# print(f.readline())
# f.flush()
# f.close()
#

# 写读模式 写完后光标在后面故而读不出来
# f = open("temp.txt","w+",encoding="UTF-8")
# print(f.readline())
# f.write("hello")
# f.flush()
# f.close()

f = open("temp.txt","a+",encoding="UTF-8")
f.write("hello")
print(f.readline())

f.flush()
f.close()






