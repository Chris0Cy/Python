from collections import Counter

def finder(arr1,arr2):
    arryOne= Counter(arr1)
    arryTwo= Counter(arr2)

    diff = arryOne - arryTwo
    
    return (list(diff.elements()))
    
