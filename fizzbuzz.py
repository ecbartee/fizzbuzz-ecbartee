# Following the assignment directions:
for i in range (1,101):
    if i %  3 == 0 and i %  5 == 0:
        print ("FizzBuzz")
    elif i %  3 == 0:
        print ("Fizz")
    elif i %  5 == 0:
        print ("Buzz")
    else:
        print (i)
        
#Playing Around - 
number = input("Can you get a FizzBuzz?  Please enter a number to see if it is divisible by 3 and 5: ")
if number.isdigit():
    number = int(number)
    print("Thank you for entering a number! Let's see if you got a FizzBuzz.  ")
    if number %  3 == 0 and number %  5 == 0:
        print ("FizzBuzz - your number is divisible by 3 and 5!")
    elif number %  3 == 0:
        print ("Fizz - your number is only divisible by 3")
    elif number %  5 == 0:
        print ("Buzz - your number is only divisible by 5")
    else:
        print ("Your number isn't divisible by 3 or 5 - try again!  No fizzbuzz for you.")
else:
    print("Please enter whole numbers only, no decimals, letters or special characters.")

