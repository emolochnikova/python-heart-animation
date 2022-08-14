from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def make_figure_heart():
    a = np.linspace(0, np.pi, 100)
    x = np.sin(a)
    y = np.sin(a) * 0.6 + np.cos(a)
    x = np.concatenate([x, -x[::-1]])
    y = np.concatenate([y, y[::-1]])
    return x, y

def make_figure_vortex():
    a = np.linspace(0, 3 * np.pi, 100)
    x1 = a * np.sin(a) / (3 * np.pi)
    y1 = a * np.cos(a) / (3 * np.pi)
    x2 = 0.8 * a * np.sin(a) / (3 * np.pi)
    y2 = 0.8 * a * np.cos(a) / (3 * np.pi)
    x = np.concatenate([x1, x2[::-1]])
    y = np.concatenate([y1, y2[::-1]])
    return x, y


x, y = make_figure_vortex()
xy1 = np.array([x, y]).T
color1 = np.array([1., 0., 0.])
x, y = make_figure_heart()
xy2 = np.array([x, y]).T
color2 = np.array([0., 0., 1.])

fps = 60.
duration = 12.
nframes = int(duration * fps)
interval_msec = int(1000/fps)

fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot()
ax.set_aspect('equal')
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.2, 1.4)

a = np.linspace(0, 2*np.pi, 100)
R = 1.
line, = ax.fill([], [], color='red')

def update_line(line, frameindex):
    k = 0.5 + 0.5 * np.sin(6 * np.pi * frameindex / nframes)
    xy = xy2 * k + (1- k) * xy1
    line.set_xy(xy)
    line.set_color(color1 * k + (1 - k) * color2)

def animate(frameindex):
    update_line(line, frameindex)
    return line,

plt.gca().set_xticks([], [])
plt.gca().set_yticks([], [])
anim = animation.FuncAnimation(fig, animate, nframes, interval=interval_msec, blit=True)
anim.save('heart-vortex.mp4')
plt.show()
