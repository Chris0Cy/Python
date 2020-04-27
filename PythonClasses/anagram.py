def anagram(s1,s2):
    listOne = s1.replace(" ", "")
    listTwo = s2.replace(" ", "")
    
    listOne = sorted(listOne)
    listTwo = sorted(listTwo)
    
    if (listOne == listTwo):
        print("testing")
    else:
        print("failed")
