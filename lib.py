##################################################################################################
#Linear algebra / mathematical / logical arrays are used from this libraries
import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)
##################################################################################################
#5*5 Numpy array comprising zeroes
c = np.zeros((5, 5))
print(c)

##################################################################################################
#2 numpy array , add the individual elements

d = np.array([1, 2, 3, 4, 5])

e = np.array([6, 7, 8, 9, 10])

f = d + e

f1 = np.sum((d, e), axis=1)

print(f1, f)

##################################################################################################
#N largest values from a Numpy array
x = np.array([12, 43, 54, 1, 100, 8, 7, 34, 68])
print(x)

y = np.argsort(x)
print(y)

z = x[np.argsort(x)[-2:][::-1]]

#to get frst two  max values from the array , by removing x from start it give only the last two index values
print(z)

##################################################################################################
#Example for creating a data fame from list and dict
import pandas as pd

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

df = pd.DataFrame(data)

print(df)

dict = {
  "fruits": ["apple", "banana", "cherry"],
  "vegetables": ["potato", "tomato", "onion"]
}

df1 = pd.DataFrame(dict)

print(df1)
##################################################################################################
#Iris dataseet extract only sepal length is gretaer than 5 & sepal width is greater than 3

read_file = pd.read_csv("iris.csv")

data = read_file.head()

print(data)

res = read_file[(read_file['sepal.length'] > 5)
                & (read_file['sepal.width'] > 3)]
print(res)

##################################################################################################
#intro NAN Values in frst 10 rowss of sepal.width & petal.length

copy_file = read_file

read_file.iloc[0:5, 2] = np.NAN

print(copy_file.head)

##################################################################################################
#get the num of NAN values present in eacj column of this nhanes dataframes

nhanes = pd.read_csv("nhanes_2015_2016.csv")

print(nhanes.isna().sum())

##################################################################################################
#read a text file and print the conetent of the file
txt = open("eg.txt", 'r')
print(txt.read())

##################################################################################################

##################################################################################################
