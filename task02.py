
def binary_search_upper(a: list[float], key: float) -> tuple[int, float]:
    """
    Binary search in sorted array of float.
    If exact match is not found, the closest biggest is returned.
    Returns number of iterations and a value. 
    """
    lower = 0
    upper = len(a) - 1
    counter = 0

    while lower < upper:
        counter += 1
        print(">> ",lower,upper)
        mid = (lower + upper) // 2
        if abs(key - a[mid]) < 1e-8:
            # if match is found with certain precision
            return (counter, a[mid])
        if a[mid] < key:
            lower = mid + 1
        else:
            # maybe we still need mid value as upper approximation
            upper = mid 
    
    if a[upper] > key:
        return (counter, a[upper])
    else:
        # if key is bigger than any element in array - task does not specify the return value
        return (counter, None) 

