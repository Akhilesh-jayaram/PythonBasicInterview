##################################################################################################
# def String():
#   str = "Akhilesh/Jayaram"
#   res = str.split("/")
#   first_name = res[0]
#   last_name = res[1]

#   print(first_name)
#   print(last_name)

# String()

##################################################################################################
#keywords are reserved special words , never use as variable name ,case sensitive eg - True False return , in ,None

#Literals are constansts used in python uses as variables -- string  , numerical -- int float long complex , boolean ---  True & False , special -- None

#variables are used to store data in python , they are case sensitive , they can be reassigned , they can

##################################################################################################
#dict is unordered collevction of elements with the key values pairs , it is mutable , it is a sequence of elements

mydict = {1: 'apple', 2: 'banana', 3: 'cherry'}
mydict1 = {
  'fruits': ['apple', 'banana', 'cherry'],
  'vegetables': ['potato', 'tomato', 'onion']
}
print(mydict, mydict1)
print(mydict.keys())
print(mydict1.values())

##################################################################################################
# # Class and objects using self method class student is created with the self method and objecrt and instance is stu1
#class is blueprint from this we built the objects that is real world entities
#cLASS IS BLUEPRINT OF THE OBJECTS , FROM THE BULUEPRINT OBJECVT IS FORMED AS A REAL WORLD ENTITUIES
#Eample##
# class human:  ###class
#     name = None
#     age = None
#     def getname(self):
#         self.name = input()
#         #print(self.name)
#     def getage(self):
#         self.age = input()
#         #print(self.age)
#     def putname(self):
#         print(self.name)
#     def  putage(self):
#         print(self.age)
# stu1 = human() ## object calling a stu1 instace of object of class human

# stu1.getage(),stu1.getname()
# stu1.putname(),stu1.putage()

##################################################################################################

# #__init is a specila method in python classes , Is a constructor method for a class
# #__init is calLED WHEN EVER AN OBJECT OF THE CLASS IS CONSTRUCTED
##used to initailizes the variables of the class

###example####
# class student:
#  def __init__(self,name,age,branch):
#    self.name =  name
#    self.age = age
#    self.branch = branch
#  def print_student(self):
#    print("name:",self.name)
#    print("age:",self.age)
#    print("branch:",self.branch)

# student = student("Ram",20,"CSE")

# student.print_student()

##################################################################################################


#inheritance - property of one class and acquiring the properties  to another class
class fruit:

  def __init__(self,color,taste):
    self.color = color
    self.taste = taste
    print("Fruit color", self.color)
    print("Fruit taste", self.taste)


#fruit = fruit("red","sweet")

class mango(fruit):
  def __init__(self):
    super().__init__("red","sweet")   ### ineherates from the supper / main class fruits
    print("Mango is a fruit")

mango = mango()

##################################################################################################


