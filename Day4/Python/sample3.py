#!/usr/bin/python

class MyClass:

    def __init__(self):
        print ("This is called as constructor")
        print ("You can initialize member vairables automatically")
        self.x = 100
        self.y = 200
   
    def setvalues(self, val1, val2):
        self.x = val1
        self.y = val2

    def printvalues(self):
        print ("Value of X is ", self.x)
        print ("Value of Y is ", self.y)
        print ("\n")

if __name__ == "__main__":
   print ("Constructing Object1")
   obj1 = MyClass()
   print ("Constructing Object2")
   obj2 = MyClass()

   print ("Before calling setvalues function")
   print ("Object Values1")
   obj1.printvalues()

   print ("Object Values2")
   obj2.printvalues()

   print ("After Calling Set values Function first time")
   obj1.setvalues(10, 20)
   obj1.printvalues()

   print ("After Calling Set values Function Second time")
   obj2.setvalues(700, 800)
   obj2.printvalues()
