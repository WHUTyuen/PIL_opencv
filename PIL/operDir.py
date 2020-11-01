import os
import sys

print(os.getcwd())

# 复制文件
with open("note/1.1.txt","r") as f, \
        open("1.1.txt" ,"w") as f2:

    f2.write(f.read())


# Iterable 可迭代的 Iterator (generator) 迭代器
#str  list set dict tuple
li = [1,2,3]
a = iter(li)
print(next(a))
print(next(a))

