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

# frequency = list(range(0,600))
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
year1_bus_travel = [22, 10, 8, 24, 18, 17] 
year2_bus_travel = [13, 45, 3, 5, 35,5]

plt.bar(["bus", "car", "bicycle", "walking", "train", "motorcycle"], year1_bus_travel, year2_bus_travel, color=["red","blue"])
plt.legend("2023", "2022")
plt.show()