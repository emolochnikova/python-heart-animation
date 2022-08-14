from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

    a = np.linspace(0, np.pi, 100)
    x = np.sin(a)
    y = np.sin(a) * 0.6 + np.cos(a + np.pi * k)
    x = np.concatenate([x, -x[::-1]])
    y = np.concatenate([y, y[::-1]])
    xy = np.array([x, y]).T

    line.set_xy(xy)

def animate(frameindex):
    update_line(line, frameindex)
    return line,

plt.gca().set_xticks([], [])
plt.gca().set_yticks([], [])
anim = animation.FuncAnimation(fig, animate, nframes, interval=interval_msec, blit=True)
anim.save('heart.mp4')
plt.show()
