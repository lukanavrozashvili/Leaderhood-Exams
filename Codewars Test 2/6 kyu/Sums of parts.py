def parts_sums(ls):
    current_sum = sum(ls)
    result = [current_sum]
    for num in ls:
        current_sum -= num
        result.append(current_sum)
    return result