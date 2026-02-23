import matplotlib.pyplot as plt
n = int(input("Enter the number of data points: "))
x = []
y = []
for i in range(n):
    x_val = float(input(f"Enter x value {i+1}: "))
    y_val = float(input(f"Enter y value {i+1}: "))
    x.append(x_val)
    y.append(y_val)
plt.scatter(x, y)
plt.xlabel("X-axis Values")
plt.ylabel("Y-axis Values")
plt.title("Scatter Plot using User Input")
plt.grid(True)
plt.show()