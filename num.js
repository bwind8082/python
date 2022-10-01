# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = [1,2,3,4]
for i in num:
 if (num % 2) != 0:
   print("{0} is Odd".format(num))
   
 else:
   print("{0} is Even".format(num))
