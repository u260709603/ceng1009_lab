# Example 1

# myList = [76, 92.3, "hello", True, 4, 76]
#
# print(myList)
# myList.append("apple")
# myList.append(76)
# print(myList)
#
# myList.insert(3, "cat")
# print(myList)
# myList.insert(0, 99)
# print(myList)
#
# print(myList.index("hello"))
#
# print(myList.count(76))
#
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)



# Example 2

# def sum_of_squares(numbers):
#     sum = 0
#     for number in numbers:
#         sum += number ** 2
#     return sum
#
# my_List = [3, 4, 5]
# print(sum_of_squares(my_List))



# Example 3

# def sum_evens(num_list):
#     sum = 0
#     for num in num_list:
#         if num % 2 == 0:
#           sum += num
#     return sum



# Example 4

# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# print(count_five_letter(["hello", "world", "world", "world", "world", "ali"]))



# Example 5

# def sum_until_even(num_list):
#     total = 0
#     for num in num_list:
#         if num % 2 == 0:
#             break
#         total +=num
#     return total
#
# print(sum_until_even([1,3, 3, 7, 5, 6, 7]))



# Example 6

# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count += 1
#         if word == "sam":
#             break
#         return count
#
# my_list = ["ali", "ahmet", "mehmet", "john", "sam" , "süleyman"]
#
# print(count_until_sam(my_list))


# Example 7

# def replace(s, old, new):
#     pieces = s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
# test(replace('Mississippi', "i", "I"), 'MIssIssIppI')



# Example 8

# def find_max_val_in_list(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# my_list = (3,2,1,0,5,7,8,10,2)
# new_list = (-34, -48, -42, -1907, -2)
# print(find_max_val_in_list(my_list))
# print(find_max_val_in_list(new_list))