# a = 50
# b = 40
#
# a+=b
# print(a)
#
# # string operations
# # len
# a = 'sangharsha'
# print(len(a))
#
# # count
# print(a.count('a'))
#
# # find
#
# print(a.find('a'))
#
# # capitalize
#
# print(a.capitalize())

# replace

# astring = 'welcome'
# print(astring.replace('c', 'd'))
#
# astring = input('enter name \n')
# substr = input('enter surname\n')
#
# first_occur = astring.find(substr)
# second_occur = astring.find(substr, first_occur+1)
#
# print(second_occur)


#############################################################################
#
# #List_operations
#
# alist = [1,3,5,True, 6, 8, 9]
# #
# # print(alist[1: : 2])
# #
# # # len
# #
# # print(len(alist))
# #
# # # sort
# # alist.sort()
# # print(alist)
#
# # reverse
# # alist.reverse()
# # print(alist)
# #
# # # append
# #
# # alist.append(17)
# # print(alist)
# #
# # # isert
# # alist.insert(3, 27)
# # print(alist)
#
# # pop
# # alist.pop(3)
# # print(alist)
#
# # remove
#
# # alist.remove(8)
# # print(alist)
#
#
# # how to reverse a list
#
# print(alist[: : -1])
#
# #####################################################################
#
# ## tuple
#
# # atuple = (1,5,3,4,5)
# #
# # # operaions
# #
# # # print(atuple.count(5))
# #
# # print(atuple.index(5))
# ################################################################
#
#
# ## dictionary
#
# adict = {
#             'name': 'Harry',
#             'marks': 100,
#             'code': 'abc200',
#             'city': 'Pune'
#          }
#
# # print(len(adict))
#
# # operations
# # items
# # print(adict.items())
# #
# # # keys
# # print(adict.keys())
#
# # update
#
# # adict.update({'city': 'sangli'})
# #
# # print(adict)
#
# # get
#
# # print(adict.get('city'))
# #
# # #####################################################################
# # ######### SET
# #
# # a = set()
#
# # print(type(a))
#
# ### set operations
#
# aset = {1,5,6,7,3,5,9,9,10}
#
# bset = {1, 9,8,9,4,5,10}
#
# # len
# print(len(aset))
#
# # union
#
# print(aset.union((bset)))
#
# # intersect
#
# print(aset.intersection(bset))
#
# # add
#
# bset.add(11)
# print(bset)
#
#
# # remove
#
# bset.remove(10)
# print(bset)
#
# # pop
# bset.pop()
# print(bset)
#
# # clear
# bset.clear()
# print(bset)



########################################################################################################

# write a program to swap to numbers

# a = 20
# b = 40
# c = a   #with temp variable
#
# a = b
# b = c
#
# print(a)
# print(b)

# how to check number is prime or not

# a = int(input('enter number'))
#
# for i in range(2, a):
#     if (a%i == 0):
#         print('number is not prime number')
#         break
#     else:
#         print("Number is prime number")
#         break

# How to factorial of number 6

# factorial = 1
#
# for i in range (1, 7):
#     factorial = i*factorial
# print(factorial)


# how to find maximum and minimum number in array??
# array--- It is list of items of same datatype

# a = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
#
# a.sort()
# print(a)
# min_item = a[0]
# print(min_item)
# max_item = a[-1]
# print(max_item)

#
# # find sum of element in list
# a = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
# sum = 0
# for i in a:
#     sum = i+sum
#
# print(sum)

# print fibonacci series

#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8.... The first two terms are 0 and 1
#  All other terms are obtained by adding the preceding two terms.

# num = 10
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")
#
# print()

#
# # Sum of items in array
#
# a = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
# sum = 0
# for i in a:
#     sum = i+sum
#
# print(sum)

# # length of list
#
# a = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
# print(len(a))

# #   how to swap first and last element in list
#
# a = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
# b = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
#
# a[0] = a[-1]
# a[-1]= b[0]
#
# print(a)


# # how to swap any two  elements in list
# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     print(list)
#
# swapPositions([1,9,8,7,5,6,3,2], 1, 4)


# # how to find nth occurance in string of given word list?
#
# input_list = ['amol', 'for', 'amol', 'amol', 'ajay', 'is', 'amol']    #
# word = 'amol'
# # n =
# # o/p == ['geeks', 'for']
#
# count = 0
# n = 4
# for i in range(0, len(input_list)-1):
#     if input_list[i] == word:
#         count = count+1
#         if count == n:
#             del input_list[i]
# print(input_list)


# # How to search an element in the list
#
# streaming = ['netflix', 'hulu', 'disney+', 'appletv+']
#
# index = streaming.index('disney+')
# print('The index of disney+ is:', index)

# # how to clear list?
#
# b = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
#
# b.clear()
#
# print(b)

# # How to reverse a list?
#
# b = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
# c = []
#
# for i in b[: : -1]:
#     c.append(i)
# print(c)

# # How to clone or copy a list
#
# b = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
#
# c = b.copy()
# print(c)

# b = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]

# # How to count occurances of element in list
#
# colors = ['red', 'blue', 'green', 7.2, 'red', 'red', 'red']
#
# for i in colors:
#     if i == 'red':
#         a= colors.count(i)
# print(a)

# # How to multiply all the numbers in the list
#
# b = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
#
# multiplication = 1
#
# for i in b:
#     multiplication = multiplication*i
# print(multiplication)

# # How to find the smallest and largest numbers on the list?
#
# a = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
#
# a.sort()
# print(a)
# min_item = a[0]
# print(min_item)
# max_item = a[-1]
# print(max_item)

# # How to find the second largest number in a list
#
# a = [2, 3, 8, 1, 5, 9, 7, 22, 61, 53]
#
# a.sort()
# a.pop(-1)
# print(a[-1])


# how to check string is palindrome is or not?
a = 'welcome'

b = ''
for i in a:
    b = i+b
    if a == b:
        print('string is palindrome')
        break
    else:
        print("string is not palindrome")
        break


##How to reverse words in a string? # extended slicing
# astring = input("enter string:")
# bstring = astring[::-1]
# print("The reverse of string is:" , bstring)


##How to find a substring in a string? (1st occurance, 2nd occurance)
# astring = input("Enter a string:")
# substring = input("Enter a substring:")
# firstoccur = astring.find(substring, 1)
# secondoccur = astring.find(substring, firstoccur+1)
# print(secondoccur)

## How to find length of string
a = 'welcome'
print(len(a))

# # How to check if the string contains any special character?
#
# a = 'welcome@123'
# s=[@,_,!, #, $, %, ^,&,*,(,),<,>,?,/,\,|,},{,~,:]
#
# if s.





















































