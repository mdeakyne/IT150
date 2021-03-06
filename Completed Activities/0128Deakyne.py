__author__ = 'Deakyne'
from datetime import datetime #This is really important
"""
This assignment is worth 10 points.  After completing the assignment, you should be able to answer
the following questions:
What do python imports help us to do?
How does the datetime module do?
How do we make printing easier?
"""
print "Problem 1--------String formatting--------------------"
"""
In this problem, you will use the datetime function to print out
A typical American format for today's date
"""

#set up the following variables, using datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

#Print out the variables as such
#<month>/<day>/<year> <hour>:<minute>:<second>

print "%s/%s/%s %s:%s:%s" % (month,day,year,hour,minute,second)

print "Problem 2------------Using datetime---------------------"
"""
Datetime has uses beyond just printing out the current time.
In this problem, we will try to print out the number of days between your birthday and today,
in effect finding how many days old you are.

Here is a link to some information on datetime: https://docs.python.org/2/library/datetime.html

You will need to follow the following steps:
1. Set todays datetime, just as you have above.
2. Create a new variable datetime, with the parameters of your birthday.
3. Use the difference operator "-" to subtract one from the other, storing it into another variable.
4. Use the .days operator to pull out the days and store it into a variable called days_old
5. Print out the days
"""
my_bday = datetime(1986,12,30)
difference = now - my_bday
#your variables here

days_old = difference.days
print "Mr. Deakyne is",days_old,"days old"
#try something here
assert(days_old > 6574), "I'm almost positive you are more than 18 years old"
