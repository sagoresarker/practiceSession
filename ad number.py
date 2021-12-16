# for loop, while
# conditional statement : if else

# greater than 35, less than 20, equal 0, equal 15, not equal -1, equal -55
"""
Debug:

"""
n = int(input())  # User input

if n > 35:
    print("Greater than 35")
elif n < 20:
    # nested if else condition
    if n == 0:
        print("Equal Zero")
    elif n == 15:
        print("Equal 15")
    elif n != -1 and n != -55:
        print("Not Equal -1")
    elif n == -55:
        print("Equal -55")
    else:
        print("Less than 20")


print("End of this program")
"""
if condition and condition:
    statement
elif condition:
    statement
elif condition:
    statement
else:
    statement

and , or
n = rice and n = pizza
n = rice or n= pizza
"""