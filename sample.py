# To find minimum and maximum number from a list using for loop and built in functions.
# print("sample python prog")
# my_list =[4,3,5,8,2,1,0,-9]
#
# i = [0]
# print(type(i))
#
# #print(my_list)
# minimum = 0
# maximum = 0
#
# for no in my_list:
#     if(no < minimum):
#         minimum = no
#     elif(no > maximum):
#         maximum = no
#
# print("Minimum value is :",minimum," And maximum value is :",maximum)

#----------------------To find the largest even and odd numbers in a list-----
import time
# my_list3 = [3,6,8,7,7,9,6,-8,7,8,1,10,11,-3]
# # maximum_even = 0
# # maximum_odd = 0
#
# max_even = max(n for n in my_list3 if(n%2 == 0)) #Used generators, we can use min, max etc. This max or min doesnt work with list comprehensions.
# max_odd = max(n for n in my_list3 if(n%2 == 1)) #Used generators
#
# print("Maximum value is {} in even numbers".format(max_even), "And Maximun value is {} in odd numbers".format(max_odd))

# #
# for n in my_list3:
#     if(n%2 == 0):
#         if(n > maximum_even):
#             maximum_even = n
#     if(n%2 == 1):
#         if(n > maximum_odd):
#             maximum_odd = n
# print("Max value in even numbers is:",maximum_even,", And Max value in Odd numbers is: ", maximum_odd)

#-----------------
#----------------- To merge two lists and sort it----------
# list1 = [5,3,7,8,9]
# list2 = [2,1,4,6,10]
#
# list3 = sorted(list1+list2)
# print((list3))

#---------------To find the middle element of a random number list--------

# elements_list = [6,7,3,9,4,8,10,11]
# sorted_list = sorted(elements_list) # This will return a sorted form of list(New)
#
# elements_list.sort() # sort() method doesn’t return any value. It will modify the original list. Reverse can be removed/added if descending order is not needed.
#
# print("Sorted list : ",sorted_list)
# print("Mid element : ",elements_list[int(len(elements_list)/2)]) #elements_list[length] gives us the total length of the list and divided by 2 gives the mid element. Sample below
# print("Through the index value... 1st position  of the sorted list: ",elements_list[1])

#--------------Four different methods to check if all items are similar in python list ----------
# #1. For loop
# def is_all_items_unique(input_list):
#     first_element = input_list[0]
#     for element in input_list:
#         if (element != first_element):
#             print(element, first_element)
#             return False
#
#     return True
#
# first_list = [1,1,1,1,1,1,1,1,2,1]
#
# if is_all_items_unique(first_list):
#     print("All elements are unique")
# else:
#     print("Not unique")

# # 2. Compare count with length
#
# first_list = [1,1,1,1,1,1,1,1,2,1]
#
# def is_all_items_unique(input_list):
# #The list.count(value) method takes one parameter value and calculates the count of it in the list or a dataframe. So, if all elements of a list are unique, list.count(list[0]) will be equal to the length of the list
#     return input_list.count(input_list[0]) == len(input_list)
#
# print(first_list.count(first_list[-2]))
# print(len(first_list))
# print(first_list[-2])
#
# if is_all_items_unique(first_list):
#     print("All items are same")
# else:
#     print("All items are not same")

## 3. using set method

##We know that a set contains only unique elements. We can create a set by passing a list as a parameter to set() constructor. It will create one new set by removing all duplicate elements from the list. So, if all the elements of our list are unique, the size of the set will be 1, isn’t it?

# first_list = [1,1,1,1,1,1,1,1,1,1]
# def is_all_items_unique(input_list):
#     return len(set(input_list)) == 1
#
# if is_all_items_unique(first_list):
#     print("All items are same")
# else:
#     print("All items are not same")


#-------------
# function to find minimum and maximum position in list
# def minimum(a, n):
#     # inbuilt function to find the position of minimum
#     minpos = a.index(min(a))
#
#     # inbuilt function to find the position of maximum
#     maxpos = a.index(max(a))
#
#     # printing the position
#     print("The maximum is at position", maxpos + 1)
#     print("The minimum is at position", minpos + 1)
#
#
# # driver code
# a = [3, 4, 1, 3, 4, 5]
# minimum(a, len(a))

# #Decorators: Its to add functionality to an existing code which will modify another part of the program at compile time.
# #This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.
# def inc(x):
#     return x + 1
#
# def dec(x):
#     return x - 1
#
# def operate(func, x):
#     result = func(x)
#     return result
#
# print(operate(inc,3))
# print(operate(dec,3))

## -------------Position Summation in List of Tuples ----------
#Eg: [(1,3),(2,5),(3,4)] -- output should be 1+2+3 and 3+5+4

# list_tuple = [(1,3),(2,5),(3,4)]
# summation = sum([i[0] for i in list_tuple]),sum([i[1] for i in list_tuple]) #This returns a tuple - One way
# print((summation))
# 
# res = [sum(i) for i in zip(*list_tuple)] #This returns a list - other way
# print((res))
#-----------Add a list to the original list------
# test_list1 = [1,2,3,4,5,6,7]
# test_list2 = [8,9,10]
# test_list1.extend(test_list2)
# t1 = test_list1.sort(reverse=True)
# print(t1)
#--------
# #-----------------Shift last element(changed to last two) to first position in list--------------------
#
# test_list1 = [1, 4, 5, 6, 7, 8, 9]
# print("Original list is", (test_list1))
#
# test_list1 =test_list1[-2:]+test_list1[:-2]
# print((test_list1))
# test_list2 = ['ironman','superman']
# test_list2 = test_list2[-1] #This returns string. If we give ":" then that returns list. eg: test_list2[-1:]
# print((test_list2[2:]))
#
# for i in test_list2:
#     print(i)
# print(type(test_list2))
# #----------
# #------------- Find frequency of given character at every position in list of lists--
# list_of_list = [[1,2,3,4],[4,5,6,7]]
# for i in list_of_list:
#     print("Length of the inner list",len(i))
#     for e in i:
#         print(e)
# print(list_of_list)
# #---------Find maximum length sub-list in a nested list------
# sub_list=[[1,2,3,4],[5,6,7,7],[1,2,3,4,5,6,7,8]]
# print(len(sub_list))
# length = 0
# lst = [max(len(i) for i in sub_list)] # using list comprehension.
# print(lst)
# #Native for loop
# for i in sub_list:
#     if(len(i) > length):
#         length = len(i)
#     else:
#         pass
# print("max list is with size",length)

# #---------Deep and shallow copy---
# # importing copy module
# import copy
# # initializing list 1
# li1 = [1, 2, [3, 5], 4]
# # using copy for shallow copy
# li2 = copy.copy(li1)
#
# # using deepcopy for deepcopy
# li3 = copy.deepcopy(li1)
#
# print(id(li1))
# print(id(li2))
# print(id(li3))
# #------------
# ----------Maximum sum of elements of list in a list of lists-------

sub_list=[[1, 2, 3], [4, 5, 6,3,11,22], [10, 11, 12], [7, 8, 9]]
# # one-way, using  list comprehension
add_list = [max(sum(i) for i in sub_list)]
print("From add_list", add_list)
temp = sum((max(sub_list)))
print("From temp variable",temp)

def maxSumList(sub_list):
    return (max(sub_list,key=sum))

print(maxSumList(sub_list))