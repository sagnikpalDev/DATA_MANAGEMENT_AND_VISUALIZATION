import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
radius = 0.5
circle = plt.Circle((1, 5), radius, color='blue')
ax.add_patch(circle)
def update(frame):
    new_x = 1 + frame * 0.1   
    circle.center = (new_x, 5)
    return circle,
ani = animation.FuncAnimation(fig, update, frames=80, interval=50)
plt.title("Animated Moving Circle (Without NumPy)")
plt.grid(True)
plt.show()