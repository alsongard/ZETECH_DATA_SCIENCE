#import matplotlib module
import matplotlib.pyplot as plt

programming_languages = [26.2 , 26.9 , 16.2, 30.6]
labels = ["java", "python", "c++", "ruby"]
color_values = ['blue', 'orange', 'green', 'red']

explode_values= (0.01, 0.01, 0.01, 0.01)
plt.figure(figsize=(10,10))
plt.pie(programming_languages, labels=labels, autopct="%1.1f%%", startangle=90, colors=color_values, explode=explode_values)
plt.title("Programming Languages")
plt.show()

#grades for data science
grades_data = [38.6, 16.44, 45.21]
label_data = ["A", "C", "B"]

plt.figure(figsize=(5,10))#plt.figure(figsize=(width, height))
plt.pie(grades_data, labels=label_data, autopct="%1.1f%%", startangle=90, colors=color_values, explode=(0.02,0.02,0.02))
plt.title("Data Science Grades")
plt.show()

communication_services = 130
consumer_staples =  130
energy = 280
health_care = 480
utilities = 50

color_vars= ["blue", "black", "red", "green", "yellow"]
plt.figure(figsize=(10,10))
plt.barh(["communication services","consumer staples","energy","health care","utilities"],[communication_services, consumer_staples, energy, health_care, utilities], color=color_vars)
plt.show()


# DISTRIBUTION PER COURSE (SEP 2023 INTAKE - ZETECH UNIVERSITY)
barchelor_bit = 130
barchelor_computer_science = 130
barchelor_se = 280
barchelor_science_cit = 490
barchelor_computerm = 50

plt.barh(["BBIT", "BCS", "BSE", "BSCIT", "BCM"], [barchelor_bit,barchelor_computer_science,barchelor_se,barchelor_science_cit, barchelor_computerm], color=color_vars)
plt.title("DISTRIBUTION PER COURSE(SEP 2023 INTAKE - ZETECH UNIVERSITY)")
plt.show()

#commuter travel in nairobi(kenya)

year_2023 = [22,13,9,25,18,17]
year_2022 = [13,47,3,5,33,4]
categories = ["bus", "car", "bicycle", "walking", "train", "motorcycle"]

#create seperate bars for each data
x1 = [i - 0.2 for i in range(len(categories))]
x2 = [i + 0.2 for i in range(len(categories))]

#plt the bar for each year
plt.bar(x1, year_2023, width=0.4, color="blue")
plt.bar(x2, year_2022, width=0.4, color="black")

#setting the labels for x-axis
plt.xticks(range(len(categories)), categories)
plt.legend(["2023","2022"])
plt.show()