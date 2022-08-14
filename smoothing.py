from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def make_figure_vortex():
    a = np.linspace(0, 3 * np.pi, 100)
    x1 = a * np.sin(a) / (3 * np.pi)
    y1 = a * np.cos(a) / (3 * np.pi)
    x2 = 0.8 * a * np.sin(a) / (3 * np.pi)
    y2 = 0.8 * a * np.cos(a) / (3 * np.pi)
    x = np.concatenate([x1, x2[::-1]])
    y = np.concatenate([y1, y2[::-1]])
    return x, y

def make_figure_heart():
    a = np.linspace(0, np.pi, 100)
    x = np.sin(a)
    y = np.sin(a) * 0.6 + np.cos(a)
    x = np.concatenate([x, -x[::-1]])
    y = np.concatenate([y, y[::-1]])
    return x, y

def smooth_up_contour(pts):
    dst = pts.copy()
    n = len(pts)
    wnd = 11

    for i in range(0, n):
        S = 0
        for j in range(0, wnd):
            S += pts[(i+j-wnd//2) % n,:]
        dst[i] = S / wnd

    return dst


fps = 60.
duration = 12.
nframes = int(duration * fps)
interval_msec = int(1000/fps)


x, y = make_figure_heart()
cont = np.array([x, y]).T
contrours_history = [cont.copy()]

for i in range(nframes - 1):
    cont = smooth_up_contour(cont)
    contrours_history.append(cont.copy())

contrours_history = contrours_history[::-1]

fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot()
ax.set_aspect('equal')
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.2, 1.4)

a = np.linspace(0, 2*np.pi, 100)
R = 1.

cont = contrours_history[0]
line, = ax.fill(cont[:,0], cont[:,1], color='red')

def update_line(line, frameindex):
    cont = contrours_history[min(frameindex, nframes - 1)]
    line.set_xy(cont)

def animate(frameindex):
    update_line(line, frameindex)
    return line,

plt.gca().set_xticks([], [])
plt.gca().set_yticks([], [])
anim = animation.FuncAnimation(fig, animate, nframes + int(fps), interval=interval_msec, blit=True)
# anim.save('heart-history.mp4')
plt.show()
