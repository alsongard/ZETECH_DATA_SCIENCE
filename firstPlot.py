import matplotlib.pyplot as plt
year = list(range(2000,2015))
print(year)
studentData = [90, 83, 72, 90, 59, 60, 79, 73, 71, 84, 91, 93, 63, 78, 82]
print(len(studentData))
print(len(year))
#plt.bar(x-axisValues,y-axisValues)
plt.bar(year, studentData)
plt.show()


apple = [0.9,0.8,0.6,0.4,1.2]
oranges = [1.3,0.3,0.7,1.1,0.8]

#to plot the data
years = list(range(2000,2005))
print(years)
print(len(years))
print(len(apple))
plt.bar(years,apple)
plt.xlabel("year of production")
plt.ylabel("apple production")
plt.title("Nairobi Apple Production")
plt.show()

#combining both to get 1 graph
plt.bar(years, apple)
plt.bar(years, oranges, bottom=apple)
plt.legend(["apples","oranges"])
plt.show()