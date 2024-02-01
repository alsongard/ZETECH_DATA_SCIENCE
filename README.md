# DATA SCIENCE ZETECH UNIVERSITY

# Description 
This file repository will be used to illustrate the use of python programmming language in data analysis.

# Features

### plt.pie()
the ``plt.pie()`` function is used to plot pie charts.It requires several arguments such as the data to be represented, label, colors, explode, autopct, startangle.
the code below will be used to explain how it works
```
        # given the data 
        import matplotlib.pyplot as plt

        programming_languages = [26.2, 26.9, 16.2, 30.6]
        labels = ["Java", "Python", "C++", "Ruby"]
        color_values = ['blue', 'orange', 'green', 'red']

        plt.pie(programming_languages, labels=labels, colors=color_values,startangle=90,  explode=[0.02, 0.02, 0.02, 0.02], autopct="%1.1f%%")
```
* programming_languages as the data to be represented.
* labels are used to label the data.
* color values is an array containing different colors.
* explode : the explode is used to set the spacing between the 4 sections of our chart.
* startangle : taes in a numerical value that is used to set at which angle the first section will start.
``autopct="%1.1f%%"``
the first symbol will be added to the data
the 1 is used to represent the width of the data to be represented.
.1 is used for setting the number of places to round of.
f is used to represent that the number should be in a floating format.

### autopct
One could also set the autopct to represent the data values as integers as shown below:
``autopct="%1.0f%%"``

