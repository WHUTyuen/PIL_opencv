import matplotlib.pyplot as plt
import numpy as np
# plt.rcParams['font.sans-serif'] = ['SimHei'] #设置黑体
# plt.rcParams['axes.unicode_minus'] = False
#
# # """画直线图"""
# # x = np.arange(10)
# # y = 3 * x
# # plt.plot(x,y,color="red",linestyle="-",linewidth="3")
# # plt.show()
#
# # """画曲线图"""
# # x = np.linspace(-3,3,100,endpoint=True)
# # y = x ** 2
# # plt.figure("曲线图")
# # plt.plot(x, y ,label="二次函数的曲线图")
# # plt.legend(loc='upper right')
# # plt.xlabel("x的取值")
# # plt.ylabel("y的取值")
# plt.title("主图")
# plt.show()

"""sin函数图像"""
# x = np.linspace(-np.pi,np.pi,60)
# y = np.sin(x)
# plt.plot(x,y)
#
# ax = plt.gca()
# ax.spines["right"].set_color('none')
# ax.spines["top"].set_color('none')
# ax.spines['left'].set_position(('data',0))
# ax.spines['bottom'].set_position(('data',0))
# plt.show()

"""动态图像"""
# x = np.linspace(-10,10,100)
# w = -5
# plt.ion()
# for i in range(100):
#     y = w * x
#     plt.clf()
#     plt.xlim(-10,10)
#     plt.ylim(-20,20)
#     plt.plot(x , y )
#     ax = plt.gca()
#     ax.spines["right"].set_color('none')
#     ax.spines["top"].set_color('none')
#     ax.spines['left'].set_position(('data',0))
#     ax.spines['bottom'].set_position(('data',0))
#     plt.pause(0.1)
#     w += 1
#
# plt.ioff()

# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
# x = np.linspace(-10,10,300)
# w = -5
# plt.ion()
# for i in range(100):
#     y = sigmoid(w*x)
#     w+=0.5
#     plt.clf()
#     plt.plot(x, y)
#     plt.pause(0.1)
# plt.ioff()

""""""
# x = np.random.randn(100)
# y = np.random.randn(100)
# plt.scatter(x,y,color="green",alpha=0.2)
# plt.show()

"""多图"""
x = np.arange(10)
y = 3 * x
plt.figure("多图")
plt.subplot(2,2,1)
plt.plot(x,y)

plt.subplot(2,2,2)
x2 = np.linspace(-3,3,20)
y2 = x2 ** 2
plt.plot(x2, y2)

plt.subplot(2,2,(3,4))
plt.plot(x,y)

plt.show()

"""
  oop
  用面向对象的思想开发一个门禁系统
  要求：
  1.系统支持访客和员工进入
  2.访客来了后可按门铃进入，员工也可以按门铃，但是还可以输入密码进入 ，还可以按指纹
  
"""