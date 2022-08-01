# 1.3
# 주어진 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목푯값을 만들 때, 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하는 프로그램을 작성하라.
# 입력값으로 주어진 배열에는 정확히 하나의 정답이 존재하며, 같은 요소의 값을 중복해서 사용할 수 없다.

## 방법1. 내꺼
# 그냥 다 찾아봄
# def twoSums(nums: list[int], target: int) -> list[int]:
#     answer = []
#     for i in range(len(nums)):
#         if i == len(nums)-1:
#             break
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 answer = [i, j]
#                 break
#         if len(answer) != 0:
#             break    
#     return answer

## 방법2. Hash Table
# Hash Table를 만들어 key:요소, value:index로 구성. target - 요소 = 다른 요소
def twoSums(nums, target):
    hash_nums = {}
    
    for i in range(len(nums)):
        value = target - nums[i]
        # hash table에서 get함수는 복잡도 가 O(1)이다. 중복을 피하기 위해 뒷부분까지 추가.
        if (hash_nums.get(value) is not None) and hash_nums[value] != i:
            # 여기서 i는 탐색 중인 
            return sorted([i, hash_nums[value]])
        hash_nums[nums[i]] = i
    
    return []


nums = [2,7,10,19]
target = 9
answer = twoSums(nums, target)

# if len(answer) == 0:
#     print("no answer available!")
# elif len(answer) == 2:
#     print("answer is " + str(answer))
