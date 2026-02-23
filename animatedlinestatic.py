import matplotlib.pyplot as plt
import matplotlib.animation as animation

x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_data = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', linewidth=2)
ax.set_xlim(0, 9)
ax.set_ylim(0, 85)

ax.set_title("Animated Line Graph")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
def init():
    line.set_data([], [])
    return line,
def update(frame):
    x = x_data[:frame]
    y = y_data[:frame]
    line.set_data(x, y)
    return line,
ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(x_data) + 1,
    init_func=init,
    interval=500,
    blit=True,
    repeat=False
)
plt.show()