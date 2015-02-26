__author__ = 'Administrator'
def checkio(words_set):
    #go through every word in the set
    for word1 in words_set:
        #go through every word other than word 1
        for word2 in words_set - {word1}:
            #get the length of the second word
            lw = len(word2)
            #word1[-lw:] will get the end of word1
            #there will be the same number of char's as word 2
            #if these equal word 2, then we've found it at the end.
            if len(word1) > len(word2) and word1[-lw:] == word2:
                #if we found it, return true
                return True

    #if we get through the whole list, and didn't find it
    #return False
    return False