# 주어진 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목푯값을 만들 때, 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하는 프로그램을 작성하라.
# 입력값으로 주어진 배열에는 정확히 하나의 정답이 존재하며, 같은 요소의 값을 중복해서 사용할 수 없다.

## 방법1. 내꺼
# 그냥 다 찾아봄
def twoSums(nums: List[int], target: int) -> List[int]:
    answer = []
    for i in range(len(nums)):
        if i == len(nums)-1:
            break
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:#            answer = [i, j]
                break
        if len(answer) != 0:
            break    


nums = [2,7,10,19]
target = 9
answer = twoSums(nums, target)
if len(answer) == 0:
    print("no answer available!")
elif len(answer) == 2:
    print("answer is " + str(answer))

## 방법2. Hash Table
# Hash Table를 만들어 key:요소, value:index로 구성. target - 요소 = 다른 요소
#nums = [2,3,8,9,11,12]
#target = 13

#hash_nums = []