#Charting in Collaboratory
import matplotlib.pyplot as plt #package used for plotting charts

x = [1,2,3,4,5,6,7,8,9]
y1 = [1,3,5,3,1,3,5,3,1]
y2 = [2,4,6,4,2,4,6,4,2]

plt.plot(x, y1, label="SEM_1")
plt.plot(x, y2, label="SEM_2")
plt.legend()
plt.title("DISTRIBUTION PER SEMESTER")
plt.xlabel("X_axis")
plt.ylabel("Y_axis")
plt.show()