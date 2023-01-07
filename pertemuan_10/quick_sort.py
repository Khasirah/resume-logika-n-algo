def quick_sort(a: list):
    result = []
    len_a = len(a)
    if len_a <= 1:
        return a
    X = a[0]
    a.pop(0)
    left_side = []
    right_side = []
    for i in a:
        if i <= X:
            left_side.append(i)
        if i > X:
            right_side.append(i)
    print(f"{left_side},{X},{right_side}")
    left_side = quick_sort(left_side)
    right_side = quick_sort(right_side)
    if len(left_side) != 0:
        for elem in left_side:
            result.append(elem)
    if len(left_side) == 0:
        result.append(X)
    
    return result

if __name__ == "__main__":
    a = [23,45,12,24,56,34,27,23,16]
    print(quick_sort(a))
