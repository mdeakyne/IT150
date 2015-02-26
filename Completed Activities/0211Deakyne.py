def tip(cost):
    return cost * 1.20

def food_tax(cost):
    return cost * 1.07

def groupon(cost):
    total = cost - 50
    if(total < 0):
        return 0
    else:
        return total
"""
The above functions have been provided for you.  Use these functions to calculate the total cost of the meal.
Remember:
tax is applied to the cost before tip.
tip is applied to the cost before groupon.
groupon subtracts after tax and tip have been applied.
"""


def total_cost(cost):
    return groupon(tip((food_tax(cost))))

print 40,total_cost(40)
assert(total_cost(40)==1.36)
print 60,total_cost(60)
print 50,total_cost(50)
print 85,total_cost(85)
"""
a number is considered a deakyne number
if it meets the following conditions:
-divisible by 3
-first and last digits are the same
-does not contain a 0
-not negative
"""
def isDeakyne(num):
    div3 = not num%3
    firstlast = str(num)[0]==str(num)[-1]
    nozero = '0' not in str(num)
    noneg = num > 0 
    return div3 and firstlast and nozero and noneg

assert(not isDeakyne(5)),"5 is not divisible by 3"
assert(not isDeakyne(-33)),"Deakyne numbers are not negative"
assert(not isDeakyne(303)), "Deakyne numbers do not contain a 0"
assert(isDeakyne(9189)),"9189 is a Deakyne number"
assert(not isDeakyne(900)),"900 is not a Deakyne number"
assert(not isDeakyne(909)),"909 is not a Deakyne number"
assert(isDeakyne(7767)),"7767 is a Deakyne number"

#find deakyne numbers and add asserts
for i in range(1,10000):
    if isDeakyne(i):
        print i
"""
give functions use them
"""
def calcAdjScore(score, scores, method):
    max_score = max(scores)
    min_score = min(scores)
    num_scores = len(scores)
    if(method == "max"):
        return score + (100 - max_score)
    elif(method == "squared"):
        return score ** .5 * 10
    elif(method == "avg"):
        return score + (max_score-min_score)/len(scores)

scores = [50,67,86,76,66,64,80]

assert(calcAdjScore(66,scores,"max")==80),"66 will get bumped up to 80 using max"
assert(round(calcAdjScore(80,scores,"squared"),2)==89.44),"80 will get bumped up to 89.44 using squared"
assert(calcAdjScore(75,scores,"avg")==80),"66 will get bumped up to 80 using avg"

print calcAdjScore(66,scores,"max")
print calcAdjScore(80,scores,"squared")
print calcAdjScore(75,scores,"avg")