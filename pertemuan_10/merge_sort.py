def merge_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a 
    
    mid = len(a)//2
    left_side = a[:mid]
    right_side = a[mid:]
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side) 
    
    return merge_two_sorted_lists(left_side, right_side)

def merge_two_sorted_lists(a,b):
    l = r  = 0
    result = []
    len_a = len(a)
    len_b = len(b)
    while l < len_a and r < len_b:
        if a[l] <= b[r]:
            result.append(a[l])
            l += 1
        else:
            result.append(b[r])
            r += 1

    while l < len_a:
        result.append(a[l])
        l += 1

    while r < len_b:
        result.append(b[r])
        r += 1

    return result

if __name__ == "__main__":
    a = [5,8,12,56, 76, 100, 102]
    b = [7,9,45,51]

    arr = [23,4,1,5,7,8,4,98,54,82,59,90,42,25,3]

    # print(merge_two_sorted_lists(a,b))
    print(merge_sort(arr))
