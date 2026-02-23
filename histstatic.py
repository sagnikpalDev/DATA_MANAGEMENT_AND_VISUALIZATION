import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 17, 19, 14]


bins = 4


plt.figure()
plt.hist(data, bins=bins)


plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Histogram (Static Inputs)")
plt.grid(True)

plt.show()