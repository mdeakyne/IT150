"""
This assignment is worth 25 points.
By the end, you should be able to answer the following questions:
How do I create a text based chose my own adventure game?
"""

"""
This assignment is worth 25 points.
By the end, you should be able to answer the following questions:
How do I make control flow from scratch?

"""

"""
Problem 1:
yesTrue has an argument ans
if ans starts with an upper or lower 'y', return True
elif ans starts with an upper or lower 'n', return False
else - leave the else how it is. I will explain what this does.
"""
def yesTrue(ans):
    if True:
        pass
    else:
        print "Enter a word that starts with y or n, please:"
        ans = raw_input()
        return yesTrue(ans)

print "Uncomment the asserts when you are ready to test problem 1"

assert(yesTrue('y')==True)
assert(yesTrue('n')==False)
assert(yesTrue("Y")==True)
assert(yesTrue("N")==False)
assert(yesTrue("No")==False)
assert(yesTrue("Yesterday")==True)
assert(yesTrue("Nothing")==False)
assert(yesTrue("brain")==True), "You would need to enter a Y word second"
assert(yesTrue("brawn")==False), "You would need to enter a N word second"



"""
Problem 2
This function will take in a word and add some flair.
save "-effing-" to a variable.
if the fist letter of word is a vowel, and the word is longer than 1 character, then insert in position 1.
else insert into the middle of the word.
return the word with the -effing- inserted.
"""
def addFlair(word):
    pass

print "Uncomment the asserts when you are ready to test problem 2"
"""
assert(addFlair("google")=="goo-effing-gle")
assert(addFlair("crown")=="cr-effing-own")
assert(addFlair("an")=="a-effing-n")
assert(addFlair("a")=="-effing-a")
assert(addFlair("energy")=="e-effing-nergy")
assert(addFlair("oppossum")=="o-effing-ppossum")
"""



"""
Problem 3
This function should use the other two functions.  It takes in two arguments: word and ans.
Word is a word you may want to insert flair into.
Ans starts with either a y or n, or it asks you to enter a y or n.
If the ans is y, it inserts -effing- according to the rules of addFlair.
If the ans is n, it just returns the word as it is.
"""
def wantFlair(word,ans):
    if(yesTrue(ans)):
        new_word = addFlair(word)
    else:
        new_word = word
    return new_word


print "Uncomment the asserts when you are ready to test problem 3"
"""
assert(wantFlair("google",'y')=="goo-effing-gle")
assert(wantFlair("crown",'y')=="cr-effing-own")
assert(wantFlair("beautiful",'n')=="beautiful")
assert(wantFlair("dumb",'n')=="dumb")
word = wantFlair("not sure","boogie")
assert(word == "not -effing-sure" or word == "not sure")
"""