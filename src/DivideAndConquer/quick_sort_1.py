"""
분할 정복 알고리즘
퀵 정렬 1
python
"""


def quick_sort(A, start, end):
    if start >= end:
        # start == end는 원소가 1개인 경우
        # start > end는 원소가 0개인 경우
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피봇보다 큰 데이터를 찾을 때 까지 왼쪽에서 이동
        while left <= end and A[pivot] >= A[left]:
            left += 1
        # 피봇보다 작은 데이터를 찾을 때 까지 오른쪽에서 이동
        while right > start and A[pivot] <= A[right]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 피봇을 교체
        if left > right:
            A[right], A[pivot] = A[pivot], A[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
        else:
            A[left], A[right] = A[right], A[left]

    quick_sort(A, start, right - 1)  # 현재 right에는 pivot 값이 위치
    quick_sort(A, right + 1, end)

    return A


A = [27, 10, 12, 20, 25, 13, 15, 22]
sorted_A = quick_sort(A, 0, len(A) - 1)
print(sorted_A)  # [10, 12, 13, 15, 20, 22, 25, 27]
