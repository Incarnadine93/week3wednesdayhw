# Create a function that given a list which represents street lights given as a parameter(l_street),
# determine if an outage has occurred.
# A street light is represented as a “T” or “F”.

# A street with a total number of “F” greater than or equal to
# 2 returns “Outage”, anything below returns “Power”

# Example Input
# [ ‘T’, ‘F’, ‘F’, ‘F’ ]
#
# Example Output:
# “Outage”


# Create a function that given a list which represents street lights given as a parameter(l_street),
# def lights(l_street):
#     t = 0
#     f = 0
#     for i in l_street:
#         if i == 'T':
#             t += 1
#         else:
#             f += 1
#     calc(t, f)

# def calc(x, y):
#     if y > x:
#         print('"Outage"')
#     else:
#         print('"Power"')

# i_lights = ['T', 'F', 'F', 'F']
# i_lights2 = ['T', 'T', 'F', 'T','T', 'F']
# i_lights3 = ['T', 'T', 'F', 'F','F', 'F','T', 'F']

# lights(i_lights)
# lights(i_lights2)
# lights(i_lights3)

# words = ['this' , 'is', 'a', 'sentence', '.']

# # def loop(list):
# #         for i in range(len(list)):
# #             x = list[i]
# #             x = x[::-1]
# #             list[i] = x

# # loop(words)
# # print(words)

# def twoPointer2(list): 
#     for i in range(len(list)):
#             x = list[i]
#             x = x[::-1]
#             list[i] = x
#     left = 0
#     right = len(list) - 1
#     while left < right:
#         list[left], list[right] = list[right], list[left]
#         left += 1
#         right -= 1
# print(words)
# twoPointer2(words)
# print(words)
##


# nums8 = [1, 3, 4, 9, 11, 18, 50, 68, 97] 
# nums9 = list(range(11))
# def binSearch(nums, target):
#     left = 0
#     right = len(nums)-1
#     while left <= right:
#         mid = (left + right)//2
#         potentialMatch = nums[mid]
#         if target == potentialMatch:
#             return f"I found your target at index: {mid}"
#         elif target < potentialMatch:
#             right = mid - 1
#         elif target > potentialMatch:
#             left = mid + 1
#     return f"Sorry, your target isn't there!!!!"
# print(binSearch(nums8, 68))
# print(binSearch(nums9, 5))
# a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# def s_dict(str):
#     dict = {}
#     w = str.split()

#     for x in w:
#         if x in dict:
#             dict[x] += 1
#         else:
#             dict[x] + 1
#     print("Word                    Quantity") 
#     print("--------------------------------")
#     for key, value in dict:
#         length = len(key)
#         space = (" " * (20-length))
#         print(f"{key}{space}${value}")

# s_dict(a_text)
# import math

# def s_dict(str):
#     dicti = {}
#     w = str.split()

#     for word in w:
#         if word in dicti:
#             dicti[word] += 1
#         else:
#             dicti[word] = 1
#     print("Word                    Quantity") 
#     print("--------------------------------")
#     for key, value in dicti.items:
#         length = len(key)
#         space = (" " * (20-length))
#         print(f"{key}{space}${value}")

l_1 = range(0, 80, 4)

def ginghoo(list, search): 
    for i in range(len(list)): 
        if list[i] == search:
            return f"The location of what you seek: {i}"


def inputnumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
    
while True:
    print("---Welcome to Ginghoo's search program---")
    while True:
        I = input("S for search, or Q for quit: ")
        if I.lower() == 'q':
            print("Thank you for letting us profit off your information")
            break
        elif I.lower() == 's':
            I = inputnumber("What number do you seek? Please input a number between 0 - 80: ")
            print(ginghoo(l_1, I))
        else:
            print("---That is not a valid input---")
    break

