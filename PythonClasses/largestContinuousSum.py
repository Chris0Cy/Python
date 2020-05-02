def large_cont_sum(arr): 
    maxValue = 0
    emptyList = []
    for i in range(len(arr)):
        if(arr[i] < 0):
            emptyList = []
        elif(arr[i]> 0):
            emptyList.append(arr[i])
            if(maxValue < sum(emptyList)):
                maxValue = sum(emptyList)
    
    return (maxValue)
