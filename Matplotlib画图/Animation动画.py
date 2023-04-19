import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    # 把0-100都传进来更新一下
    line.set_ydata(np.sin(x+i/100))
    return line,


def init():
    line.set_ydata(np.sin(x))
    return line,


ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)
# func表示animation更新的方式（简洁：可以用lambda函数）；frames=100表示animation的长度（100帧）；init_func表示动画的最开始的一帧；
# interval表示update的频率，隔多少ms更新一次；blit=False更新整张图片，True更新变化的部分

plt.show()
