"""
This assignment is worth 25 points.
By the end, you should be able to answer the following questions:
How do I make control flow from scratch?
How do I write a helper function?

"""

"""
Problem 1
"""
def yesTrue(ans):
    if(ans[0].lower()=='y'):
        return True
    elif(ans[0].lower()=='n'):
        return False
    else:
        print "Enter a word that starts with y or n, please:"
        ans = raw_input()
        return yesTrue(ans)

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
"""
def addFlair(word):
    ef = "-effing-"
    if word[0] in ['a','e','i','o','u'] and len(word)>1:
        ins = 1
    else:
        ins = len(word)/2
    return word[:ins]+ef+word[ins:]

assert(addFlair("google")=="goo-effing-gle")
assert(addFlair("crown")=="cr-effing-own")
assert(addFlair("an")=="a-effing-n")
assert(addFlair("energy")=="e-effing-nergy")
assert(addFlair("a")=="-effing-a")
assert(addFlair("oppossum")=="o-effing-ppossum")

"""
Problem 3
"""
def wantFlair(word,ans):
    if(yesTrue(ans)):
        return addFlair(word)
    else:
        return word

assert(wantFlair("google",'y')=="goo-effing-gle")
assert(wantFlair("crown",'y')=="cr-effing-own")
assert(wantFlair("beautiful",'n')=="beautiful")
assert(wantFlair("dumb",'n')=="dumb")
word = wantFlair("not sure","boogie")
assert(word == "not -effing-sure" or word == "not sure")


