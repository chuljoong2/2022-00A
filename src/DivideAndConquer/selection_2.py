"""
분할 정복 알고리즘
선택 문제 2
python
"""


def selection(A, k):
    if len(A) <= 1:
        return A[0]

    pivot_value = A[0]
    tail = A[1:]

    leftList = [x for x in tail if x <= pivot_value]
    rightList = [x for x in tail if x > pivot_value]

    sgs = len(leftList)

    if k == sgs + 1:
        return pivot_value
    elif k <= sgs:
        return selection(leftList, k)
    elif k > sgs:
        return selection(rightList, k - sgs - 1)


A = [8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
seleted_number = selection(A, 9)
print(seleted_number)  # 12
