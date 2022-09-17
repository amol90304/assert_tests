## Syntax error v/s exceptions

# Exceptions is raised when program is synexically correct but code resulted in error

# some of the excpetions

# vaue error
# out of index error
# name error
# no module error

# a = [10,20,30,40,55]
#
# print(a[1])
# print(a[6])

# Handle such eceptions we use try and except blocks

# a = [10,20,30,40,55]
#
# try:
#     print(a[1])
#     print(a[3])
#     print(a[2])
#     print(a[6])
#     print(a[7])
# except Exception as detail:
#     print("Program has not error except", detail)
#
#
# print("Hello brother ")

# try:
#     a = int(input("enter number", ))
#     result = 100/a
#     a = [10, 20, 30, 40, 55]
#     print(a[6])
# except IndexError as detail1:
#     print("program is ok except", detail1)
# except ZeroDivisionError as detail2:
#     print("program is ok except", detail2)
# except ValueError as e1:
#     print("Generic Exception---", e1)
#
# except Exception as e:
#     print("Generic Exception---", e)


# try:
#     a = 10
#     b = 25
#     c = a+b
#     assert c == 35
# except Exception as e:
#     print("Exeption handled")
# else:
#     print("No exception")
#
# finally:
#     print("Everything is fine")

























