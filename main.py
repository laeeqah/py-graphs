import matplotlib.pyplot as plt


test_scores = [12,99,65,85,42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo","Ziyaad" ]

x_position = [i for i, _ in enumerate(test_names)]

plt.bar(x_position, test_scores, color='blue')
plt.xlabel("name")
plt.ylabel("Marks(%)")
plt.title("Python Marks for 5 students")
plt.xticks(x_position, test_names)
plt.show()

