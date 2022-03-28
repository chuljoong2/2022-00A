"""
분할 정복 알고리즘
합병 정렬
python
"""


def merge_sort(A):
    if len(A) <= 1:
        return A

    k = len(A) // 2
    leftList = merge_sort(A[:k])
    rightList = merge_sort(A[k:])

    return merge(leftList, rightList)


def merge(leftList, rightList):
    result = []

    while len(leftList) > 0 and len(rightList) > 0:
        if leftList[0] > rightList[0]:
            result.append(rightList.pop(0))
        else:
            result.append(leftList.pop(0))

    if len(leftList) > 0:
        result.append(leftList.pop(0))
    if len(rightList) > 0:
        result.append(rightList.pop(0))

    return result


A = [27, 10, 12, 20, 25, 13, 15, 22]  # unsorted
sorted_A = merge_sort(A)
print(sorted_A)  # [10, 12, 13, 15, 20, 22, 25, 27]
