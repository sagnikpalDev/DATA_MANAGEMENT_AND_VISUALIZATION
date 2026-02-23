import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [10, 15, 13, 17, 20, 18, 25, 22]
plt.scatter(x, y)
plt.xlabel("X-axis Values")
plt.ylabel("Y-axis Values")
plt.title("Scatter Plot using Static Inputs")
plt.grid(True)
plt.show()