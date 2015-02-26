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

assert(round(total_cost(40),2)==1.36),"check your order - tax, then tip, then groupon"
assert(round(total_cost(60),2)==27.04)
assert(round(total_cost(50),2)==14.20)
assert(round(total_cost(85),2)==59.14)

"""
a number is considered a deakyne number
if it meets the following conditions:
-divisible by 3
-first and last digits are the same
-does not contain a 0
-not negative
"""
def isDeakyne(num):
    condition1 = num > 0
    condition2 = True
    condition3 = "0" not in str(num)
    condition4 = True

    return condition1 and condition2 and condition3 and condition4 #need to build the condition.

assert(not isDeakyne(5)),"5 is not divisible by 3"
assert(not isDeakyne(-33)),"Deakyne numbers are not negative"
assert(not isDeakyne(303)), "Deakyne numbers do not contain a 0"
assert(isDeakyne(9189)),"9189 is a Deakyne number"
assert(not isDeakyne(900)),"900 is not a Deakyne number"
assert(not isDeakyne(909)),"909 is not a Deakyne number"
assert(isDeakyne(7767)),"7767 is a Deakyne number"

"""
People did very poorly in an advanced IT test, and Deakyne needs to curve the grades.
The scores are below, and you have max, min and num score variable to work with.
the method can be max, squared or avg
max : the new score recieves 100-max extra points
squared: the new score is the square root of the old score * 10
avg: the new score is the score plus the high score minus the low score divided by number of scores.
otherwise: return the original score.
Don't mess with the scores variable below.
"""
def calcAdjScore(score, scores, method):
    max_score = max(scores)
    min_score = min(scores)
    num_scores = len(scores)
    if(method == "max"):
        return formula_for_new_score


    return score

#don't change the scores here.
scores = [50,67,86,76,66,64,80]

assert(calcAdjScore(66,scores,"max")==80),"66 will get bumped up to 80 using max"
assert(round(calcAdjScore(80,scores,"squared"),2)==89.44),"80 will get bumped up to 89.44 using squared"
assert(calcAdjScore(75,scores,"avg")==80),"66 will get bumped up to 80 using avg"
assert(calcAdjScore(75,scores,"bird")==75),"75 will remain the same, doesn't understand this method"
