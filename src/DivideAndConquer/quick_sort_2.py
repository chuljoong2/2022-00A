"""
분할 정복 알고리즘
퀵 정렬 2
python
"""


def quick_sort(A):
    if len(A) <= 1:
        return A

    pivot = A[0]  # 피봇은 첫 번째 원소 (인덱스 아님)
    tail = A[1:]  # 피봇을 제외한 리스트

    leftList = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    rightList = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    return quick_sort(leftList) + [pivot] + quick_sort(rightList)


A = [27, 10, 12, 20, 25, 13, 15, 22]
sorted_A = quick_sort(A)
print(sorted_A)  # [10, 12, 13, 15, 20, 22, 25, 27]
