from itertools import combinations

def pair_sum(arr,k):
    comb = combinations(arr,2)
    newList= []
    counter = 0;
    
    for sets in comb:
        if sum(sets) == k:
                counter += 1
                newList.append(sets)
    print (newList)
    return counter
