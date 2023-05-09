# Write a Python program that takes a list of strings as
#  input and outputs the number of times each string 
# appears in the list, using a dictionary and conditional
#  statements.
def stringed(list):
    {string:list.count(string) for string in list}
    stringed()
    # stringed("God","is","love")


# Write a Python program that takes a list of numbers 
# as input and outputs the median of the numbers 
def programmed(numbers):
   numbers.median(numbers)
#    return median
programmed(numbers)
    # programmed()



# Write a Python program that takes a list of numbers 
# as input and outputs the second largest number in 
# the list using conditional statements and a for loop.
def second_largest(numbers):
    largest = None
    second_largest = None
    for nums in numbers:
        if largest is None or nums > largest:
            second_largest = largest
            largest = nums
        elif second_largest is None or nums > second_largest:
            second_largest = nums
    return second_largest

numbers = [5, 10, 15, 20, 25]
print(second_largest(numbers))


# Write a Python program that takes a year as input 
# and determines if it is a leap year.


# Write a Python program that takes a string as input
#  and checks if it is a palindrome (reads the same 
# forwards and backwards), ignoring spaces and punctuation.