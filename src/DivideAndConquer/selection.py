"""
분할 정복 알고리즘
선택 문제
python
"""


def selection(A, k):
    pivot, start, end = 0, 0, len(A) - 1
    left = start + 1
    right = end

    while left <= right:
        while left <= end and A[pivot] >= A[left]:
            left += 1
        while right > start and A[pivot] < A[right]:
            right -= 1

        if left < right:
            A[left], A[right] = A[right], A[left]
        else:
            A[pivot], A[right] = A[right], A[pivot]
            pivot = right

    sgs = pivot - start

    if k == sgs + 1:
        return A[pivot]
    elif k <= sgs:
        return selection(A[start:pivot], k)
    elif k > sgs:
        return selection(A[pivot + 1:end + 1], k - sgs - 1)


A = [8, 3, 11, 9, 12, 2, 6, 15, 18, 10, 7, 14]
seleted_number = selection(A, 9)  # k = 9
print(seleted_number)  # 12
