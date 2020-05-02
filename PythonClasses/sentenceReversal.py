def rev_word(s):
    emptyString = ""
    wordList = s.split(' ')
    wordList.reverse()

    for i in wordList:
        if(i != ''):
            emptyString += (i + " ")
    
    print (emptyString)
