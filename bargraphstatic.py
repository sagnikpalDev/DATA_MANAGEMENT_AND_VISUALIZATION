import matplotlib.pyplot as plt


categories = ["Math", "Science", "English", "History"]
values = [85, 90, 78, 88]


plt.figure()
plt.bar(categories, values)


plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Bar Graph (Static Inputs)")
plt.grid(axis='y')

plt.show()