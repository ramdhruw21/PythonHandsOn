'''    Classes are created by keyword class.
       Attributes are the variables that belong to a class.
       Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
'''
class Empty:
    pass 


'''
Objects:-
The object is an entity that has a state and behavior associated with it.

An object consists of:

    State: It is represented by the attributes of an object. It also reflects the properties of an object.
    Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
    Identity: It gives a unique name to an object and enables one object to interact with other objects.
'''

obj = Empty()

'''
     self == this in java, cpp
     __init__ == Constructor in java, cpp
'''

class Dog:
    
    # Class Attributes
      attr1 = "mammal"

    # Instance attribute
      def __init__(self, name):
           self.name = name
         