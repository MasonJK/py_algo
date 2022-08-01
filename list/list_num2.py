# 1.4
# 정렬되 배열의 요소들을 중복 없이 단 1번씩만 가질 수 있도록 주어진 배열을 그대로(in-place) 수정하고, 수정된 배열의 새로운 길이를 반환해라
# 추가적인 배열의 할당은 하지 않고, 중복된 요소를 하나만 남기고 걸러내는 함수를 만드는 것. 반환된 길이 이후에 있는 데이터는 무시해도 무방

def eliminate_repetition(nums: list[int]) -> list[int]:
    memory = []
    for i in range(len(nums)):
        if nums[i] in memory:
            del nums[i]
        else:
            memory.append(nums[i])
    return nums

nums = [0,0,0,1,1,1,2,2,2]
eliminate_repetition(nums)