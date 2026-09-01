def merge(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    i = 0
    j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort_helper(arr, left, right):

    if left == right:
        return

    mid = (left + right) // 2

    merge_sort_helper(arr, left, mid)
    merge_sort_helper(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge_sort(arr):
    if len(arr) > 1:
        merge_sort_helper(arr, 0, len(arr) - 1)
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 역순
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = merge_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 중복 원소
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("=== 테스트 케이스 4: 중복 원소 ===")
    print(f"정렬 전: {arr4}")
    result4 = merge_sort(arr4.copy())
    print(f"정렬 후: {result4}")


