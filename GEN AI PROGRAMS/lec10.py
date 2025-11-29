'''Matplotlip-- it is a python library, it is use for data visualization.
Import matplotlib.pyplot as plt
        library    submodule  alias
'''
#matplotlib , lineplot
import matplotlib.pyplot as plt
import numpy as np

'''xpoint = np.array([1,9])
ypoint = np.array([2,4])
plt.plot(xpoint, ypoint)
plt.show()'''

'''cgpa = np.array([6,8,8,9,9.5,9.7,10])
package = np.array([4,4,9,9,4,6.8,10])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(cgpa,package, "*:b", ms=15 , mec= "red", linewidth=3, mfc="yellow")
plt.xlabel("CGPA", fontdict=font1)
plt.ylabel("PACKAGE",fontdict=font2)
plt.title("CGPA VS PACKAGE", fontdict=font1)
plt.grid()
plt.show()'''

#bar plot -- it work on numerical as well as categorical data
'''fruit = np.array(["Apple", "Banana", "Orange", "Watermelon"])
fruit_number = np.array([100, 80, 50,40])
color = ["red", "yellow", "orange", "green"]
plt.barh(fruit, fruit_number, color = color)
plt.show()'''

#pie plot
'''x = np.array([35, 76,69,88])
my_labels = np.array(["Apple", "Banana", "Orange", "Watermelon"])
my_explode = [0.2, 0, 0 , 0]
plt.pie(x, labels = my_labels , explode = my_explode)
plt.legend(title = "Fruit" , loc = "lower right")
plt.show()'''

#scatter plot-- it works on numerical data to get information in dot patterens
'''x = np.array([1,2,3,4,5,6,7,8])
y = np.array([200,180,160,150,130,120,110,100])
plt.xlabel("Age of car")
plt.ylabel("Speed of car")
plt.title("Scatter plot")
plt.scatter(x,y)
plt.show()'''

#histogram plot-- A histogram shows frequency distribution
'''x = np.random.randint(40,100,(1,200))
x = x.flatten()
print(x)
plt.xlabel("Marks of Students")
plt.ylabel("Number of Students")
plt.title("Histogram plot")
plt.hist(x, bins=15)
plt.show()'''

