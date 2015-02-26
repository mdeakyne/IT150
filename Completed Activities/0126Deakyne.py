__author__ = 'Deakyne'
"""
This assignment is worth 10 points.  After completing the assignment, you should be able to answer
the following questions:
How do you make a string variable?
What are indexes?
How do we access a single character of a string?
What does the len function do?
What does the upper function do?
What does the lower function do?
What is casting?
How do we cast an integer to a string?
How do we add strings together?
What does %s do?
How do we get input from users?
"""

print "Problem 1-----------------------------------------------"
#Fill in these variable names with values that are true for you.
name = "Mr. Deakyne"
major = "Computer Science"
sport = "Frisbee Golf"
age = "28"
alphabet = "abcdefghijklmnopqrstuvwxyz"


assert(name != ""),"Put something in the name variable"
assert(major != ""),"Put something in the major variable"
assert(sport != ""),"Put something in the sport variable"
assert(age != ""),"Put something in the age variable"
assert(alphabet == "abcdefghijklmnopqrstuvwxyz"),"Don't you know the alphabet?"

print "Wow, %s you are only %s? Maybe playing %s makes you look older. How is studying %s going?" % (name,age,sport,major)
print "The 10th letter of the alphabet is %s" % (alphabet[9]) #remember, start counting at 0

print "Problem 2-----------------------------------------------"
#Use the guidelines of the assert statements to set the following variables.
#Some you will have to be more creative than others.

shortest_string = ""
teacher = "Mr. Deakyne"
actor = "Maconahay"
word = "tremendous"
food = "pizza"
superhero = "flash"

assert(len(shortest_string)==0),"Your shortest string can be shorter"
assert(teacher == "Mr. Deakyne"), "Watch the capitals, and period"
assert(actor[0]=="M" and len(actor)>7), "Need an actor starting with M, with a name longer than 7 letters"
assert(word[9]=="s"), "Check the index, and make sure its 9"
assert(food[2] == food[3] == 'z'), "What food has two z's in the middle?"
assert(superhero[-1]=='h'), "-1 refers to the LAST index. This is a python trick. What must the last letter be?"

print "While watching the %s movie and eating %s, I thought to myself, 'I'm more %s than %s'." % (superhero,food,word,actor)
print "Problem 3-----------------------------------------------"
#Use len, upper, lower, and str to pass the assert statements
len_name = len("Matthew Deakyne") #replace with your name first
upp_quote = "i have no idea what we are yelling about".upper()
low_quote = "WE MUST USE OUR INDOOR VOICES".lower()
str_check = str(4582) #Do not just add quotes

assert(type(len_name)==type(1)), "Don't forget to use len."
assert(upp_quote == "I HAVE NO IDEA WHAT WE ARE YELLING ABOUT"), "Need to make the string uppercase"
assert(low_quote == "we must use our indoor voices"), "Need to make the string lowercase"
assert(str_check == "4582"),"Make this int into a str, without just adding quotes"

print "Problem 3 finished."
print "Problem 4-----------------------------------------------"
#I've given you snippets of a sentence.  Add them together and store them into the correct_order variable

a = "you can do it."
b = "a great teacher, a"
c = " good online textbook, and"
d = "Learning to code"
e = " if you have"
f = " is actually not too hard "
g = "a lot of patience. I know "
correct_order = d + f + e + b + c + g + a #use the variable names and add the strings together

for part in [a,b,c,d,e,f,g]: #we will learn about for loops later on, don't worry about this.
    assert(part in correct_order),"Missing part %s" %(part)
print correct_order


print "Problem 5-----------------------------------------------"
#Take user input and store it into the three variables below.
#Then print out in the following format listed below.

print "What is your name?"
name = raw_input() #take in user input
print "What is your favorite movie?"
movie = raw_input()
print "Write in any adjective:"
adjective = raw_input()

#now, print out something with the following format.
#"Thanks for recommending <movie>, <name>! I'll watch it the next time I'm <adjective>."

print "Thanks for recommending %s, %s! I'll watch it the next time I'm %s" % (movie, name, adjective)

assert(name != ""),"You didn't enter a name!"
assert(movie != ""), "You didn't enter a movie!"
assert(adjective != ""),"You didn't enter an adjective!"
print ""
print "!!! The assignment is complete, please turn it in on eSpire !!!".upper()
print ""