"""
This assignment is worth 10 points and you should be able to answer the following questions after completing it:
What is the difference between a variable and a literal?
How do you assign variables in python?
How do you deal with errors in python?
What are different types of python variables?
How do you make a multiline comment?
How do you handle exponents in python?
What does % do in python?
"""

print "\nProblem 1----------------Errors-----------------------------" 
#In this lab, you will deal with many errors. IndentErrors and NameErrors are the most common.
#Many times, it's because you've mispelled a variable you did define.
#Below there are three errors for you to deal with. Do not delete any lines, just add to the below code.
#You may edit the names of variables.

print "The variable name contains",name 

def printName():
name = "Deakyne"
print "The variable name contains",name

printName()
print "The variable name contains",nmae

print "\nProblem 2----------------Comments--------------------------"
#These are all comments.
Make this into a comment


Instead
Of
Commenting
Out
Every
Line
Here
You
Can
Quickly
Comment
Multiple
Lines.
Please
Do
So.

print "Done with comments"
print "\nProblem 3----------------Literals vs. Variables---------------"
"This is a literal" # a literal is anything that only has one value.
variable = "This is a variable" # a variable can have many values, and can be reassigned.
variable = "Something different" # our variable has been reassigned a new value.

#below we have a variable named a and a literal 'b'. Add another variable b, and give it any value

a = 'b'

print "The variable a contains",a 
print "The variable b contains",b 
print "The literal a prints as",'a' 
print "The literal b prints as",'b' 




print "\nProblem 4-----------------Types-----------------------------"
#We will be introducing more types later in the course. Here are four variables, have python print the types
#As a reminder, you can use the type    function. I'll refresh your memory.

f = 3.14
i = 7
s = "Hello there"
b = False

print "The type of printName is",type(printName)
print "The type of f is",type()  #fill in these with the appropriate variable, following the example above
print "The type of i is",type()
print "The type of s is",type()
print "The type of b is",type()

print "\nProblem 5------------------Math----------------------------"
#Codecademy introduced *, +, -, /, ** and %
#Use them to figure out the following, and print the result

print "3243 + 23424 =",
print "10^2",  #did you use python syntax?
print "10 / 6=",  #double check this one, why is there no remainder?
print "10 % 6=",  #Oh, that's where the remainder went.
