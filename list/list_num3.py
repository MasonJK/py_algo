# 정렬된 배열과 목푯값이 주어지는데 목푯값을 찾는다면 배열의 해당 인덱스를 반환하고,
# 찾지 못한다면 정렬된 배열이 되도록 목표값이 배열에 들어가야 하는 인덱스를 구하는 문제다.

# 복잡도: O(N)
def my_answer(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    
# 복잡도: O(logN). 정렬된 배열을 보면 이진탐색을 무조건 고려해봐야된다.
def my_binary_search_answer(nums, target):
    start = 0
    end = len(nums)-1
    while True:
        mid = int((start+end)/2)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if nums[mid] == target:
            return mid
        if nums[mid]<target<=nums[mid+1]:
            return mid+1
        if nums[mid] < target:
            start = mid
        else:
            end = mid

def book_binary_search_answer(nums):
    
    
nums = [1,4,5,6]
target = 0
# print(my_answer(nums, target))
print(my_binary_search_answer(nums, target))