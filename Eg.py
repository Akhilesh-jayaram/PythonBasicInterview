#################################################################################################
#lAMBDA fUNCTION IS A ANANONYMOUS FUNCTION , IT IS A FUNCTION WITHOUT A NAME , IT IS A SMALL ANONYMOUS FUNCTIOn Systax Lambda arguments : Expressions
#create a lambda Function to add 10 to a given number

x = lambda a: a + 10

print(x(10))

#################################################################################################
#create a simple line plot , where x and y axis values range from 0-10.Title is "Y vs X",x-axis label is "x-axis" and y-axis labels is "y-axis"
# import numpy as np
# from matplotlib import pyplot as plt

# x = np.arange(0, 10, 1)

# print(x)
# y = x

# plt.plot(x, y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Time Vs Distance")
# plt.show()
# #################################################################################################
# #Create a simple bar plot like xaxis has names of fruits and yaxis has cost of fruits

# data = {"Fruits": ["Apple", "Mango", "Banana", "Grapes","Blueberry"], "Cost": [200, 300, 100,400,150]}

# namesFruits = list(data["Fruits"])
# costFruits = list(data["Cost"])
# plt.bar(namesFruits, costFruits)
# plt.show()

#################################################################################################
#Module helps in logically organizing our python code , it is a file containing python definitions and statements  eg --- calclutor program
#randomize trhe items of a list in place in python , we can randomize the items of a list in place using the random.shuffle() function

from random2 import shuffle

x = ["mary", "had", "a", "little", "lamb"]
shuffle(x)
print(x)

#################################################################################################
#get the length of the string without len() function
string = "ophthalmology"
count = 0
for i in string:
  count = count + 1
print(count)

#################################################################################################
#Replace all the odd numbers in this Numpy array  to -1
import numpy as np

arr = np.arange(0, 15)

arr[arr % 2 == 1] = -1

print(arr)
#################################################################################################
#get Common items between two Numpy arrays
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

array_two = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print(np.intersect1d(array, array_two))

#################################################################################################
#Covert the first character of each elements in a pandas series to upper case
import pandas as pd

data = pd.Series(["Mary", "had", "a", "little", "lamb"])

data = data.str.capitalize()

#rint(data)

data = data.map(lambda x: x.capitalize())
print(data)
#################################################################################################
#Calculate the number of characters in each word in a series
code = pd.Series(["Mary", "had", "a", "little", "lamb"])

#code = code.str.len()
#print(code)

code = code.map(lambda x: len(x))
print(code)
#################################################################################################
#iris dataframe , change the column name Sepal.length to S_length

read = pd.read_csv("iris.csv")
print(read.head())
newdata = read.rename(columns={'sepal.length': 'S_length'})
print(newdata)

#################################################################################################
#Build linear regression model on this Botson Dataframe , independent variable rm & dependent varaible medv . the train and test split needs 80:20 ratio
botson = pd.read_csv("housing.csv")

data = botson.head()

print(data)

rm = pd.DataFrame(data["RM"])  #features
medv = pd.DataFrame(data["MEDV"])  #teaget
#split into trrain & test
from sklearn.model_selection import train_test_split

rm_train, rm_test, medv_train, medv_test = train_test_split(rm,
                                                            medv,
                                                            train_size=0.80)
#build model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(rm_train, medv_train)

medv_pred = regressor.predict(rm_test)

from sklearn import metrics

print("Root mean squared error is :",
      np.sqrt(metrics.mean_squared_error(medv_test, medv_pred)))

#################################################################################################
#build a decison tree classifier  model on this iris dataframe where dependent variable is species and independent variables are rest of the columns trin and test split should be 70:30

iris = pd.read_csv("iris.csv")
data = iris.head()
print(data)
all = pd.DataFrame(data[['sepal.length','sepal.width','petal.length','petal.width']])
species = pd.DataFrame(data["variety"])

all_train , all_test , species_train , species_test = train_test_split(all,species,train_size=0.70)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(all_train,species_train)

species_pred = classifier.predict(all_test)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(species_test,species_pred))

from sklearn.metrics import accuracy_score
print(accuracy_score(species_test,species_pred))
#################################################################################################

