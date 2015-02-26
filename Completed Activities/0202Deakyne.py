"""
This assignment is worth 10 points.
By the end, you should be able to answer the following questions:
What are the comparison signs?
How do you evaluate conditionals?
How do you compare two strings?
How do and, or and not work?
What does an if do?
What does elif do?
What does else do?

"""
print "Problem 1: ------------ands, ors, nots--------------------"
"""
Without editing the variables a through h, edit the assert statements
to pass.  On a test, you will not get to run code as a check, so
make sure you understand why these are true or false.
"""


a = True
b = False
c = a or b
d = c and b
e = a and c or d
f = d or not c
g = not b
h = e and g

assert(a == True), "This is just an example"
assert(b == False), "Another example"
assert(c == True)
assert(d == False)
assert(e == True)
assert(f == False)
assert(g == True)
assert(h == True)
#add asserts for the rest, using True and False - not typing in the conditions.

print "Did you add in asserts for c through h?"
print "Problem 2:------------comparing numbers---------------------"
"""
Edit the if , elif, else statement to do the following:
if num 1 is greater : print "<num1> is greater than <num2>"
elif num2 is greater : print "<num2> is greater than <num1>"
else : print "<num1> equals <num2>"
"""
print "Enter 1st number"
num1 = raw_input()
print "Enter 2nd number"
num2 = raw_input()

num1, num2 = int(num1),int(num2)
if(num1 > num2):
    print num1,"is greater than",num2
elif(num2 > num1):
    print num2,"is greater than",num1
else:
    print num1,"equals",num2

print "Try entering several different entries"
print "PRO TIP: After you are done, you can comment out a problem, to skip it when testing"
print "2nd PRO TIP: Remember to UNCOMMENT before you submit."
print "Problem 3:----------------comparing size----------------------"
"""
Use raw_input to take in a word from the user
Add an if, elif, else statement to do the following:
If the word is shorter than 5 letters, print out "The word is short"
If the word is between 5 and 10 letters, print out "That's a great length"
If the word is more than 10 letters, print out "No need to get all fancy!"
Hint: Use len(word) and compare it.  Also use "and"
"""
print "Enter a word: "
word = raw_input()
if(len(word)<5):
    print "The word is short"
elif(len(word)>=5 and len(word)<=10):
    print "That's a great length"
else:
    print "No need to get all fancy!"

print "Try entering several different entries"

print "Problem 4:---------------Functions as conditionals ---------"
"""
This is a bit tricky, but I bet you are all smart enough to handle this.

I've given you three functions which check simple things.
Your job is to use these functions in an if statement.
"""

def long_enough(password):
    if len(password) < 10:
        return False
    else:
        return True

def starts_upper(password):
    if password[0].isupper():
        return True
    else:
        return False

def ends_number(password):
    if password[-1].isdigit():
        return True
    else:
        return False

"""
Use the above functions to test if a users password meets the standards.
Just to be clear, these are not great standards. These use code we understand, though
so they will have to do.

Have a user input their password to check.
Print out "Password is secure" if it is long enough, starts with an upper case and ends in a number.
Otherwise, print out "Change your password, it is not secure!"
"""
print "Enter your password: "
password = raw_input()
if(long_enough(password) and starts_upper(password) and ends_number(password)):
    print "Password is secure"
else:
    print "Change your password, it is not secure!"

print "Check this with various passwords, especially those that should fail"
