__author__ = 'Matthew'


print "Problem 1 : --------------iteration---------------------------------------"
lost = [2,4,8,15,16,32,42]
banana = "My spoon is too big."
rankings = {"Deakyne":"The best", "Hughes":"No comment","Philpot":"Hard","King":"Pretty Great"}

for item in lost:
    print item

for char in banana:
    print char

for teacher in rankings:
    print teacher, rankings[teacher]

#go through each data type with a for loop:
#1: print the current item, for dictionaries, print the key and the value.


print ""
print "All items should print on a new line above"

print "Problem 2 :-----------------Counting-----------------------------------------"
#We can count the number of times something occurs in a list by using a for and an if.
#fill out the following function to count the number of A's in the example class
#don't forget to use values of a dictionary, rather than keys


def countA(class_grades):
    count = 0
    for student in class_grades:
        if class_grades[student] == "A":
            count += 1
    return count

grades = {"Bob":"A","Stu":"B","Ron":"A","Ken":"D","Bill":"A","Jill":"A","Tom":"B","Joe":"C"}
assert(countA(grades)==4),"1st check Remember to compare against values"
grades = {"Bob":"A","Stu":"A","Ron":"A","Ken":"A","Bill":"A","Jill":"A","Tom":"B","Joe":"C"}
assert(countA(grades)==6),"2nd check Use variables, don't just solve it for one case"
grades = {"Bob":"C","Stu":"B","Ron":"F","Ken":"D","Bill":"A","Jill":"B","Tom":"B","Joe":"C"}
assert(countA(grades)==1),"Final Check"
print "All tests passed on problem 2"

print "Problem 3:--------Dictionaries are powerful------------------------------------"
"""
You can store anything as a value in dictionaries, including functions!
This is pretty crazy when you think about it.
I've given you three functions, store them in a dictionary d, with string names of functions as keys
"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def exp(a,b):
    return a**b

d = {"add":add, "sub":sub, "div":div, "mod":mod, "exp":exp} #add the rest in.
assert(d["add"](4,3)==7),"Add function needs to be in d"
assert(d["sub"](5,6)==-1),"Sub function needs to be in d"
assert(d["div"](4,3)==1),"Div function needs to be in d"
assert(d["mod"](10,3)==1),"Mod function needs to be in d"
assert(d["exp"](4,3)==64),"Exp function needs to be in d"

#Now, go through every function in d, and apply print out key, a,b and value
#don't make this a function, but make sure it prints something like:
#order doesn't matter.
"""
add 4 5 9
sub 4 5 -1
div 4 5 0
mod 4 5 4
exp 4 5 1024
"""
a = 4
b = 5
#add code here
for f_name in d:
    print "%s %s %s %s" % (f_name,a,b,d[f_name](a,b))


print "Make sure to print out"
print "Problem 4:--------This Lesson Brought to you by Applebees----------------------"
"""
READ THIS CAREFULLY. You probably want to read it about 3 times.
I've provided three lists, appetizers, drinks and entrees
Each item in these lists is also in the prices dictionary.

There is another dictionary below called "deals".  Deals has a day as a key and A FUNCTION as a value.
This works the same way as problem 3.
I've given you one of these functions as an example.

You have to complete 3 functions below:
    item_in_entrees
    item_in_drinks
    get_price

Get price works as such:
start total at 0
go through every item in order
if that item is a deal item, it is half off
add the cost of the item to the total
return the total, rounded to 2 decimal places

YOU ARE ONLY CHANGING THINGS WHERE I'VE PUT 'add your code here'
"""


appetizers = ["crunchy onion rings","app sampler","sweet potato fries and dips", "brew pub pretzels & dip"]
drinks = ["whiskey smash", "old fashioned", "fireball whiskey lemonade", "domestic beer"]
entrees = ["bourbon street steak","sizzling skillet fajitas","sizzling double barrel whisky sirloins",
           "bourbon street chicken and shrimp", "shrimp & broccoli cavatappi"]

prices = {
    "crunchy onion rings":6.99,
    "app sampler":15.99,
    "sweet potato fries and dips":5.99,
    "brew pub pretzels & dip":5.99,
    "whiskey smash":6.99,
    "old fashioned":7.99,
    "fireball whiskey lemonade":7.99,
    "domestic beer":4.00,
    "bourbon street steak":20.50,
    "sizzling skillet fajitas":18.99,
    "sizzling double barrel whisky sirloins":22.99,
    "bourbon street chicken and shrimp":17.99,
    "shrimp & broccoli cavatappi":16.99
}

def item_in_apps(purchase):
    return purchase in appetizers

def item_in_entrees(purchase):
    return purchase in entrees

def item_in_drinks(purchase):
    return purchase in drinks

deals = {
    "Friday":item_in_apps,
    "Saturday":item_in_entrees,
    "Sunday":item_in_drinks
}

def get_price(order,day):
    total = 0
    for item in order:
        if deals[day](item):
            total += prices[item] * .5
        else:
            total += prices[item]
    return round(total,2)

order = ["bourbon street steak","shrimp & broccoli cavatappi", "domestic beer","app sampler"]
assert( get_price(order,"Friday")==49.48),"1st test - something went wrong"
assert( get_price(order,"Saturday")==38.73),"2nd test - make sure not to hardcode"
assert(get_price(order,"Sunday"==55.48)),"3rd test - almost there"

