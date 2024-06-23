def sum_consecutives(lst):
    if not lst:
        return []
    
    result = []
    current_sum = lst[0]
    
    for i in range (1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_sum += lst[i]
        else:
            result.append(current_sum)
            current_sum = lst[i]
    
    result.append(current_sum)
    
    return result