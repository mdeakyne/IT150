"""
Lab 2
This lab is worth 25 points.
It covers the following topics:
Python arithmetic.
Assert statements.
Variables.
Print statements.
Comments
"""

print "Problem 1----------------------Assert Statements-------------"
"""
This problem is worth 10 points
change the following assert statements so they do not throw and error
DO NOT CHANGE THE VARIABLES, change the assert statements
"""
t_add = 5 + 7
t_sub = 10 - 18
t_div = 18 / 5
t_mod = 18 % 5
t_exp = 2**3

assert(t_add == 0), "Your add assert is wrong"
assert(t_sub == 0), "Your sub assert is wrong"
assert(t_div == 0), "Your div assert is wrong"
assert(t_mod == 0), "Your mod assert is wrong"
assert(t_exp == 0), "Your exp assert is wrong"

print "Problem 2---------------------Variables-----------------------"
"""
This problem is worth 10 points

Use 5 variables to describe the following scenario:
A teacher has 200 points to give out to three students.
The teacher decides to give out each student a third of the points.
A fourth student says they want some points.
The teacher decides to take back 10% from every other student.
The first two students don't make a fuss, but the third refuses.
The teacher gives the collected points to the fourth student.
How many points do the teacher and four students have at the end?
Your teacher variable should have 4 different values at various points in the story.
Declare and update your variables to tell the entire story.

Print out the results at the end
"""

#teacher to 200
#student_1 = teacher / 3.0
#student 2
#student 3
#teacher to no points

#teacher reclaim points from 1st two students
#student1
#student2

#student 4 = teacher
#teacher has no points


#check your work:
#first student and second student should have 60 points
#third student should have 66.66 repeating points
#fourth student should have 13.33 repeating points
#teacher should have no points.


print "Problem 3--------------------Comments---------------------------"
"""
This problem is worth 5 points
Look over the following code and make comments making up a story for the
following variables.  You may use line by line comments or one big comment.

Model it after my comments for problem 2 above.
"""

Deakynes = 1000

Meal = 50
Tax = .0675
Tip = .20
Deakynes = Deakynes - (Meal+Meal*Tax)*(1+Tip)

Crib = 40
Baby_books = 20
Sales_tax = .05
Deakynes = Deakynes - ((Crib+Baby_books)*(1+Sales_tax))

Buy_In = 500
Odds_to_win = (6/4.0)
Win = True
Deakynes = Deakynes + Buy_In * Odds_to_win

Celebratory_Drinks = 40
Uber_ride_home = 60
Tip = .15
Deakynes = Deakynes - Celebratory_Drinks * (1+Tip) - Uber_ride_home * (1+Tip)

print Deakynes