__author__ = 'Bret'
"""
1. statements write your own asserts
"""

"""
This problem is worth 10 points
change the following assert statements so they do not throw and error
DO NOT CHANGE THE FUNCTIONS, change the assert statements
"""
def f_add(a,b):
    return a+b

def f_sub(a,b):
    return a-b

def f_div(a,b):
    return a/b

def f_mod(a,b):
    return a%b

def f_exp(a,b):
    return a**b

assert(f_add(5,7) == 12), "Your add assert is wrong"
assert(f_sub(10,18) == -8), "Your sub assert is wrong"
assert(f_div(18,5) == 3), "Your div assert is wrong"
assert(f_mod(18,5) == 3), "Your mod assert is wrong"
assert(f_exp(2,3) == 8), "Your exp assert is wrong"


"""
2. Here you are creating a calculator that takes in 3 arguments.
a and b are the operators and the operation is a string which contains
"add", "sub", "div", "mod" or "exp".
"""
def calculator(a,b,operation):
    if (operation == "add"):
        return f_add(a,b)
    elif (operation == "sub"):
        return f_sub(a,b)
    elif (operation == "div"):
        return f_div(a,b)
    elif (operation == "mod"):
        return f_mod(a,b)
    elif (operation == "exp"):
        return f_exp(a,b)
    else:
        return "I don't understand that operation"

assert(calculator(2,3,'exp') == 8), "You changed my exp portion."
assert(calculator(2,4,'ret') == "I don't understand that operation"), "You changed my else"
assert(calculator(10,18,'sub') == -8), "Your sub portion is wrong"
assert(calculator(4,6,'add') == 10), "Your add portion is wrong"
assert(calculator(18,5,'div') == 3), "Your div portion is wrong"
assert(calculator(19,5,'mod') == 4), "Your mod portion is wrong"
"""
3. write your own funciton.
call the function "f_root" and take in numbers a and b.
you should take the b root of a.
Use exponents and division to complete the root.
"""
#your function here

def f_root(a,b):
    return a**(1.0/b)


assert(f_root(25,2)==5), "The 2nd root of 25 is 5"
assert(f_root(8,3)==2), "The 3rd root of 8 is 2"
assert(round(f_root(17,4),2)==2.03), "The 4th root of 17 is 2.03"