"""
In today's assignment, you are completing three functions that work as follows:

1. def count_letter(l_words,letter):
input : l_words - list of words , letter - single character
output: num - the number of words containing that letter

Process:
Start the count at 0
Go through each word in the list of words.
Check if the letter is in the word
If the letter is in the word, add 1 to the count
Return the count

2. def compare_letters(l_words,letter1,letter2):
input: l_words - list of words, letter1 - single character, letter2 - single character
output: 1, 0 or -1 .  1 - letter1 occurs in more words, 0 - they both appear in the same number, -1 - letter2 appears in more words

Process:
Get the count of each letter in the list of words
Use an if, elif, else, comparing the two counts
Return the correct choice based on the comparisons


3. def percentages(l_words,letters):
input: l_words - list of words, letters - a string of characters
output: print out the percentage for each letter :
                number of words the letter occurs in / number of words in the list
        print it out in the following format : "<letter> occurs in <percentage>% of words in the list"

Process:
Go through each letter in letters
    Get the count of each letter
    Divide that count by the length of l_words
    Print out "<letter> occurs in <percentage>% of words in the list"

You will have to test these functions on your own.
"""

def count_letter(l_words, letter):
    count = 0
    for word in l_words:
        if letter in word:
            count += 1
    return count

def compare_letters(l_words,letter1,letter2):
    count_let1 = count_letter(l_words,letter1)
    count_let2 = count_letter(l_words,letter2)

    if count_let1==count_let2:
        return 0
    elif count_let1 > count_let2:
        return 1
    else:
        return -1


def percentages(l_words,letters):
    for letter in letters:
        count_let = count_letter(l_words,letter)
        percentage = float(count_let)/len(l_words) * 100
        print "%s occurs in %s of words in the list" % (letter,percentage)


#function calls
words = ["this","should","be","ok","once","you","get","the","hang","of","it"]

print count_letter(words,'o')
print compare_letters(words,'e','o')
percentages(words,"shbokyg")