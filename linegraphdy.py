import matplotlib.pyplot as plt


n = int(input("Enter number of data points: "))

x_values = []
y_values = []


for i in range(n):
    x = float(input(f"Enter x value {i+1}: "))
    y = float(input(f"Enter y value {i+1}: "))

    x_values.append(x)
    y_values.append(y)


plt.figure()
plt.plot(x_values, y_values, marker='o')


plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Graph (User Input)")
plt.grid(True)

plt.show()