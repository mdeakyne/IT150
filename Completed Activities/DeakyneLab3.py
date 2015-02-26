__author__ = 'Matthew'
from datetime import datetime
#Problem 1: 7 points
"""
Write out code that takes one input from the user: An 8 digit number.
Since we don't know how to error check, your program will have errors if someone enters a number less than 8 digits.

Do the following with this number:
store the numbers 1 and 2 into a variable.
store the numbers 3 and 4 into a variable.
store the numbers 5,6,7 and 8 into a variable.

Convert all the variables from strings to ints. To turn things into type <str> we use srt(var),
how do you think we turn things into type <int>?

print out three statements in the following format:
Replace your var name with the literal name, and the two variables with string formatting.
"Variable (your var name) contains <variable>, which is of type <variable type>"
"""
print "Enter an 8 digit number"
inp = raw_input()
a = inp[0]+inp[1]
b = inp[2]+inp[3]
c = inp[4]+inp[5]+inp[6]+inp[7]

a = int(a)
b = int(b)
c = int(c)

print "Variable a contains %s, which is of type %s" % (a,type(a))
print "Variable b contains %s, which is of type %s" % (b,type(b))
print "Variable c contains %s, which is of type %s" % (c,type(c))

#Problem 2: 7 points
"""
Look up the day the university starts the semester, and the last day of finals. Figure out how many days are in between.

print out a string of the following format:
"In Spring of 2015, there are <variable> days in our semester"
"""
start = datetime(2015,1,10)
end = datetime(2015,5,7)
day_diff = (end - start).days

print "In Spring of 2015, there are %s days in our semester" % (day_diff)

#Problem 3: 11 points
"""
Combine the skills you used for the two problems above, and write code that asks the user for two days in the following
format: DDMMYYYY.  You should have two prompts - the start day and the end day.  Use these inputs to make two
datetime objects, and calculate the difference in days.

print out the following:

"There are <variable> days between the dates <variable> and <variable>"
"""
print "Enter a start day in the format MMDDYYYY"
date1 = raw_input()
print "Enter an end day in the format MMDDYYYY"
date2 = raw_input()

day1 = int(date1[2]+date1[3])
mon1 = int(date1[0]+date1[1])
year1 = int(date1[4]+date1[5]+date1[6]+date1[7])

day2 = int(date2[2]+date2[3])
mon2 = int(date2[0]+date2[1])
year2 = int(date2[4]+date2[5]+date2[6]+date2[7])

start = datetime(year1,mon1,day1)
end = datetime(year2,mon2,day2)
day_diff = (end - start).days


print "There are %s days between the dates %s and %s" %(day_diff, start,end)