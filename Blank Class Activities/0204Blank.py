"""
This assignment is worth 10 points.
By the end, you should be able to answer the following questions:
How does slicing work?
How do we construct strings?
"""

print "Problem 1----------Pig Latin--------------------"
"""
We are going to take in a word from the user and do quite a bit with it.
First, though, lets review pig-latin - with a variation.

Instead of turning horse into orsehay, we will turn it into orse-hoy
student becomes tudent-soy. We also are going to be using functions,
even though codecademy hasn't covered this in depth yet.

It'll be ok, I promise.
"""

def piglatin(original):
#change this code to use oy, and the hyphen.
#also, we are going to count 'y' as a vowel.
    pyg = 'ay'

    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        if first in ['a','e','i','o','u']:
            new_word=word+pyg
            return new_word

        else:
            new_word=word[1:]+word[0]+pyg
            return new_word
    else:
        return 'empty'

assert(piglatin("")=='empty'),"Check for empty string"
assert(piglatin("123")=='empty'),"Check against numbers"
assert(piglatin("student")=='tudent-soy'),"Modify to use oy and hyphen"
assert(piglatin("horse")=='orse-hoy')
assert(piglatin("amoeba")=='amoeba-oy'),"Make sure you change the vowel return too."
assert(piglatin("yesterday")=='yesterday-oy'),"Y is a vowel too."
print "Passed all tests on problem 1"
print "Problem 2 --------------Word play--------------------"
"""
Pig latin is so boring. Instead, we want to switch words up.
We will edit two functions to do so.
"""

def firsttolast(word):
    #switch up the first and last letters and return the new word.
    if (len(word) #fill in this part):
        return word

    new_word = ""
    return new_word

assert(firsttolast("check")=="khecc"),"work on first to last"
assert(firsttolast("Teacher")=="reacheT")
assert(firsttolast("a")=="a")
assert(firsttolast("of")=="fo")
assert(firsttolast("bae")=="eab")

def switchatmiddle(word):
    middle = len(word)/2
    new_word = ""
    return new_word

assert(switchatmiddle("hello"))=="llohe","work on switchatmiddle"
assert(switchatmiddle("nope")=="peno")
assert(switchatmiddle("of")=="fo")
assert(switchatmiddle("a")=="a")
assert(switchatmiddle("racecar")=="ecarrac")

print "See, that wasn't too bad.  Good job using string slices. Turn in your file."
