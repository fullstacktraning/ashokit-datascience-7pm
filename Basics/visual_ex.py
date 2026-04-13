import matplotlib.pyplot as plt

# Example-1
# x = [1,2,3,4]
# y = [10,20,25,30]
# plt.plot(x,y)
# plt.plot(x,y,color="red")
# plt.plot(x,y,color="blue",linestyle="--")
# plt.plot(x,y,color="red",marker="o")
# plt.xlabel("Input Values")
# plt.ylabel("Results")
# plt.title("Simple Line Plot")
# plt.show()

# Example - 2
# x = [1,2,3,4,5]
# y1 = [10,20,30,40,50]
# y2 = [15,25,35,20,55]
# plt.plot(x,y1,color="red",marker="o",label="Plot1")
# plt.plot(x,y2,color="green",marker="o",label="Plot2")
# plt.xlabel("Input Value") 
# plt.ylabel("Output")
# plt.title("Multiple Plots")
# plt.legend()
# plt.show()

# Example-3
# students = ["A", "B", "C", "D", "E", "F", "G", "H"]
# study_hours = [2, 3, 5, 6, 8, 1, 4, 7]
# marks = [40, 50, 65, 70, 90, 35, 60, 80]

# colors = []
# for m in marks:
#     if m >= 75:
#         colors.append("green")
#     elif m>= 50:
#         colors.append("blue")
#     else:
#         colors.append("red")


# plt.title("Student Performance Analysis")
# plt.xlabel("Study Hours")
# plt.ylabel("Marks")
# plt.scatter(study_hours,marks,color=colors)

# for i in range(len(students)):
#     plt.text(students[i])

# plt.grid(True)
# plt.show()


# Example-4
# Bar Chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 25000, 18000, 30000, 28000, 22000]
max_sale = max(sales)
min_sale = min(sales)
colors = []
for s in sales:
    if s == max_sale:
        colors.append("green")
    elif s == min_sale:
        colors.append("red")
    else:
        colors.append("blue")
plt.figure(figsize=(8,5))
plt.bar(months,sales,color=colors)
for i in range(len(months)):
    plt.text(i,sales[i],str(sales[i]),ha="center")
plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()