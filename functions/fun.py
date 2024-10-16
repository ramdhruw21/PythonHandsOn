# Creating Function

def my_funtion():
    print("Hello World!")

my_funtion()

# Information passed into function as Arguments

def my_function(fname):
    print("My name is " + fname)

my_function("Ram Dhruw")

"""
        Parameters & Arguments
        A parameter is the variable listed inside the parentheses in the function definition
        An argument is the value that is sent to the function when it called
"""
# 1 Simple Arguments 
def my_function(fname, lname):
    print("My name is " + fname +" " + lname)

my_function("Ram", "Dhruw")

## 2 Arbitary Arguments(*) - Using *args pass many arguments (tuple of arguments)

def args_funtion(*kids):
    print("The youngest child is " + kids[2])

args_funtion("Emily", "Bunty", "Raju", "Monu")


## 3 Keyword Arguments - key = value (order of arguments does not matter)

def keyword_function(child1, child2, child3):
    print("The youngest child is " + child1)

keyword_function(child1="Emily", child2="Monu", child3="Raju")


## 4 Arbitary keyword argumnets - **kwargs it will take many keyword arguments (dictionary of arguments)

def args_kyw_fun(**kid):
    print("His last name is " + kid["lname"])

args_kyw_fun(fname="Ram", lname = "Dhruw")

## 5 Default parameter value 

def my_country(country="Norway"):
    print("I am from " + country)

my_country()
my_country("India")
my_country("USA")
my_country("Brazil")

## 6 Passing List as a Arguments - send any types of arguments to a function (string, number, list, dictionary etc.) and it will treated as a same data type inside the function

def my_function(food):
    print(food[0])
    for x in food :
        print(x)

food = ["apple", "banana", "cherry"]

my_function(food)


## 7 Return Value 
def my_function(x, y):
    result = x+y
    return result*5
print(my_function(4, 5))


## 8 Pass Statement - function definition cannot be empty, but for avoiding error put pass keyword
def fun():
    pass


## 9 Postional-ONLY Arguments ( , /) - specify that a function can have ONLY positional arg. or ONLY  keyword arg.

def fun(x, /):
    print(x)

fun(3)

## Keyword args but expects postional args 
def fun(x):
    print(x)

fun(x = 23)

## 10 Keyword-ONLY Arguments (*, )



