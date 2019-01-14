# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# num = 0
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = ax.plot([], [], 'r-', animated=False)

# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,

# def update(frame):
#     global num
#     if(num % 5 == 0):
#         ax.set_xlim(0, num * np.pi)
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     num = num + 1
#     return ln,

# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

num =[0 for _ in range(91)]
xaxes = [x for x in range(0, 91)]
fig = plt.figure() 
axes1 = fig.add_subplot(111) 
line, = axes1.plot(xaxes, num) 
axes1.set_ylim(0,1.1) #设置y轴范围
plt.xticks([]) #关闭x轴刻度

#因为update的参数是调用函数data_gen,
#所以第一个默认参数不能是framenum 
def update(data): 
  line.set_ydata(data) 
  return line, 
# 每次生成10个随机数据 
def data_gen():
    global num 
    while(True):
        num = num[1:] + [np.random.rand(1)]
        yield num
ani = animation.FuncAnimation(fig, update, data_gen, interval=200, blit=True)
plt.show()