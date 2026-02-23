import matplotlib.pyplot as plt
import matplotlib.animation as animation
start_x = float(input("Enter starting X position: "))
start_y = float(input("Enter starting Y position: "))
radius = float(input("Enter radius of circle: "))
speed = float(input("Enter speed (movement per frame): "))
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
circle = plt.Circle((start_x, start_y), radius, color='blue')
ax.add_patch(circle)
def update(frame):
    new_x = start_x + frame * speed
    circle.center = (new_x, start_y)
    return circle,
ani = animation.FuncAnimation(fig, update, frames=80, interval=50)
plt.show()



