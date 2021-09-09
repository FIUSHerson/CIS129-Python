from typing import final


fruits = ("apple","banana","cherry")
print("The fruits are: " + str(fruits))

(a,b,c) = fruits
print("The fruits are: {}, {}, and {}. ".format(a, b, c), end='')

number_collection = (1,2,3,4,5,6,7,8,9)
final_string = ""
for i in number_collection:
    final_string  = final_string + "{} ".format(i)
print(final_string)