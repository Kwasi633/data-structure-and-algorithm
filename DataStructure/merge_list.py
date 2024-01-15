def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    Divide: Find the endpoint of the list and divide into sublists
    Conquer:  Merge the sorted sublists created in previous step
    0(n log n)
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

"""
Divide the unsorted list at midpoint into sublists
Returns two sublists - left and right.
Takes overall O(log n) time
"""
def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges 2 lists(arrays), sorting them in the process
    Returns a new merged list
    (0log time)
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 26, 93, 17, 77, 31, 44, 55, 8, 20, 12]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
    

#3.30