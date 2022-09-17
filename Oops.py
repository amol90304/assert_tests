# class --- class is logical entity. It contains method, attributs
# object--- It is physical entity. It is intantiation of class

# # simple class with simple object
#
# class Demo:
#     def fun1(self):
#         print("Everything fine")
#
# obj = Demo()
# obj.fun1()

# instance method and static method

# class Demo:   # instance method
#     def fun1(self):
#         print("everything fine")
#
#
#     @staticmethod
#     def fun2():
#         print("Everything Okay")
#
# obj2 = Demo()
# obj2.fun1()
# Demo.fun2()


# # local class and global variables
#
# a = 20
# b = 40
#
# class Demo:
#     a = 200
#     b = 500
#     def fun3(self, a, b):
#         print(self.a+self.b)
#         print(a+b)
#         print(globals()['a']+globals()['b'])
#
# obj = Demo()
#
# obj.fun3(500, 400)
#
# # how to find id of object
# print(id(obj))



######################################################################
# constructor

# __init__ is special methond which invoke as soon as object gets created for class

# class Demo:
#
#     def __init__(self, a, b):
#         print("Hello")
#         self.a = a
#         self.b = b
#
#     def method1(self):
#         print(self.a+self.b)
#
# obj = Demo(100, 200)
#
# obj.method1()


# How to call one method into another method

# class Demo:
#
#     def __init__(self, a, b):
#         print("Hello")
#         self.a = a
#         self.b = b
#
#     def method1(self):
#         print(self.a+self.b)
#
#     def method2(self):
#         self.method1()
#         print("New method get access")
#
# obj =Demo(150,350)
# obj.method2()



#
# obj = Demo(100, 200)
#
# obj.method1()


## split names

# ename = input("Enter name\n")
#
# elist = ename.split()
#
# first_name = elist[0]
# second_name = elist[1]
# last_name = elist[2]
#
# first_initial = first_name[0]
# second_initial = second_name[0]
#
# print(f"{first_initial} {second_initial} {last_name}")

















