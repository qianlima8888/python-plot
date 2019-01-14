import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

num =[0 for _ in range(91)]
xaxes = [x for x in range(0, 91)]
fig = plt.figure() 
axes1 = fig.add_subplot(111) 
line, = axes1.plot(xaxes, num) 
axes1.set_ylim(-180, 180) #设置y轴范围
plt.xticks([]) #关闭x轴刻度


def update(data): 
  line.set_ydata(data) 
  return line, 

def data_gen():
    global num 
    for line in open("/home/wode/yaw.txt"):
        num = num[1:] + [float(line)]
        yield num
        #line = f.readline()
ani = animation.FuncAnimation(fig, update, data_gen, interval=100, repeat=False)
plt.show()