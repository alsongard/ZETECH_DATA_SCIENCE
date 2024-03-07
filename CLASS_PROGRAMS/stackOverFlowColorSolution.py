import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#Make the color you want
Color = np.array([0.5, 0.6, 0.7])#not a must to specify the zeroes
print(Color)

#Make some data:
Vals = np.random.uniform(size = (10,3))#generates 10 rows each with 3 columns
print(Vals)
print(Vals.shape)

PointCount = Vals.shape[0]#take number of rows from the shape result
print(PointCount)

Xvals = Vals[:, 0]#used indexing and slicing to select all rows and follwoed by columns
Yvals = Vals[:, 1]#used indexing and slicing to  select all rows and followed by column 1
Zvals = Vals[:, 2]

#2 reprocude the issue
# fig = matplotlib.pyplot.figure()
# subplot = fig.add_subplot(111)
# matplotlib.pyplot.scatter(Xvals, Yvals, c=Color)

#Solution
ValsCount = Vals.shape[0]
ColorsRepeated = np.repeat(np.atleast_2d(Color), ValsCount, axis=0)
print("ColorsRepeated")
print(ColorsRepeated)

#2D: MAKE scatter plot without warning issue using repeat()
fig = plt.figure()
subplot = fig.add_subplot(111, projection="3d")
plt.scatter(Xvals, Yvals, Zvals, c=ColorsRepeated)
plt.show()