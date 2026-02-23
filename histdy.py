import matplotlib.pyplot as plt
n = int(input("Enter number of data values: "))
data = []
for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    data.append(value)

bins = int(input("Enter number of bins: "))
plt.figure()
plt.hist(data, bins=bins)

plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Histogram (User Input)")
plt.grid(False)

plt.show()