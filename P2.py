# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single
# line.
# Suppose the following input is supplied to the program: 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def fact1(number):
    factorial = 1  # Initialize factorial to 1, not 0
    while number > 0:
        factorial = factorial * number  # Multiply, not add
        print(number)
        number -= 1 
    return(factorial)

print("hekko")
print(fact1(5))
