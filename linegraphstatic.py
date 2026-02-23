import matplotlib.pyplot as plt

# Static data points
x_values = [0, 1, 2, 3, 4, 5]
y_values = [0, 1, 4, 9, 16, 25]

# Create line graph
plt.figure()
plt.plot(x_values, y_values, marker='o')

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Graph (Static Inputs)")
plt.grid(True)

plt.show()