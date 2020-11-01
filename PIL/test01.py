
import os

print(os.getcwd())
# 连接两个目录组成一个新的路径 /
imgpath= os.path.join(os.path.dirname(os.getcwd()),"img\\temp.txt")
f = open(imgpath)
print(f.readline())
f.close()

for i in os.listdir(os.path.dirname(imgpath)):
    print(i)

for i in os.listdir(os.path.abspath("../img")):
    print(i)


# 取当前的目录的绝对路径
print(os.path.abspath("../../.."))

# and or not

def createDirAndFile(dirPath, fileName):
    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)
    if not os.path.isfile(fileName):
        f = open(fileName,'w')
        f.close()
    else:
        return True

dirPath = os.path.dirname(os.getcwd()) + "\\note"
print(dirPath)

for i in range(10):
    createDirAndFile(dirPath,dirPath+"\\{}.0.txt".format(i+1))

#
s = "abcd"
s = s.replace("b","e")
print(s)
def renameFile(dirPath):
    i = 0
    li = os.listdir(dirPath)
    li.sort(key=lambda x : int(x[0:x.index(".")]))
    for e in li:
        s = e.replace(".{}.".format(e.split(".")[1]),".{}.".format(i+1))
        print(e,s)
        i+=1
        os.rename(dirPath+"\\"+e, dirPath+"\\"+s)

renameFile(dirPath)

