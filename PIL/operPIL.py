from PIL import Image,ImageFilter,ImageDraw,ImageFont
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("../img/pic.jpg")
# img.show()
# shape 为 width,height
# n、c、h、w
# h、w、c
print(img.size)

print(img.getbands())
a = np.array(img)
print(a)

print(list(img.getdata()))

"""加特效"""
# 轮廓滤波
# img =img.filter(ImageFilter.CONTOUR)
# img.show()
#
# img = img.filter(ImageFilter.BLUR)
# img.show()


# img = img.filter(ImageFilter.BoxBlur(radius=50))
# img.show()

# img = img.filter(ImageFilter.DETAIL)
# img.show()

# 高清大图 锐化
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()
#
# img = img.filter(ImageFilter.EMBOSS)
# img.show()

# img = img.convert("L")
# # img.show()
# pixel = img.getpixel((300,400))
# print(pixel)
# print(img.getbands())
# img = img.convert("RGB")
# # img.show()
# print(img.getbands())
# pixel = img.getpixel((300,400))
# print(pixel)

# img2 = img.copy()
# img2.show()

# 调整尺寸
# img = img.resize((200,300))
# img.show()

# 等比缩放
# w ,h = img.size
# img.thumbnail((w//2,h//2))
# img.show()
# print(img.size)
#
# logo = Image.open("../img/pic1.jpg")
# img.paste(logo, (100,200))
# img.show()

# """抠图"""
# img = img.crop((300,400,400,500))
# img.show()

"""split() 分割层"""
r,g,b = img.split()
print(r)
print(g)
print(b)

# r.show()
# g.show()
# b.show()





"""灰度直方图"""
img = Image.open("../img/validatecode.jpg")
img = img.convert("L")
his = img.histogram()
print(his)
plt.subplot(2,1,1)
plt.imshow(img)
plt.axis("off")
plt.subplot(2,1,2)

# plt.plot(list(range(256)),his)
plt.hist(np.array(img).flatten(),bins=256)
plt.show()

# img = img.rotate(30)
# img.show()
# img.save("../img/pic2.jpg")
import random

"""做验证码"""
def gen_code():
    return chr(random.randint(65,90))

def backgroundcolor():
    return (random.randint(90,160),random.randint(90,160),random.randint(90,160))

def foregroundcolor():
    return (random.randint(60,120),random.randint(60,120),random.randint(60,120))

width,height = 240,60
def getPanel():
    return Image.new("RGB",(width,height),color=(255,255,255))

def validateCode():
    panel = getPanel()
    font = ImageFont.truetype("C:\Windows\Fonts\BRLNSDB.TTF",36)
    draw = ImageDraw.Draw(panel)
    for y in range(height):
        for x in range(width):
            draw.point((x,y),fill=backgroundcolor())

    for i in range(4):
        draw.text((i*60+15,15),fill=foregroundcolor(),text=gen_code(),font=font)
    panel.show()
    panel.save("../img/validatecode.jpg")


# validateCode()
