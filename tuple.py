#Create a Tuple:
tuple1 = ("apple", "banana", "cherry")
print(tuple1)

#Tuples allow duplicate values:

tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple1)

#To determine how many items a tuple has, use the len() function:
tuple1 = ("apple", "banana", "cherry")
print(len(tuple1))

#One item tuple, remember the comma:

tuple2 = ("apple",)
print(type(tuple2))

#NOT a tuple
tuple3 = ("apple")
print(type(tuple3))

#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple4 = (1, 5, 7, 9, 3)
tuple5 = (True, False, False)


#A tuple with strings, integers and boolean values:

tuple6 = ("abc", 34, True, 40, "male")

#Using the tuple() method to make a tuple:

tuple7 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tuple7)

