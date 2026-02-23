import matplotlib.pyplot as plt
import matplotlib.animation as animation
x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_data = [0, 2, 1, 3, 5, 4, 6, 5, 7, 8]
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
line, = ax.plot([], [], marker='o')
def update(frame):
    line.set_data(x_data[:frame], y_data[:frame])
    return line,
ani = animation.FuncAnimation(fig, update, frames=len(x_data)+1, interval=500)
plt.title("Animated Line (Google Colab)")
plt.grid(True)
plt.show()