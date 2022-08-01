# 1.4
# 정렬된 배열의 요소들을 중복 없이 단 1번씩만 가질 수 있도록 주어진 배열을 그대로(in-place) 수정하고, 수정된 배열의 새로운 길이를 반환해라
# 추가적인 배열의 할당은 하지 않고, 중복된 요소를 하나만 남기고 걸러내는 함수를 만드는 것. 반환된 길이 이후에 있는 데이터는 무시해도 무방

# 추가적인 배열 할당했음
# def eliminate_repetition(nums):
#     memory = []
#     i = 0
#     while True:
#         if i == len(nums):
#             break
#         if nums[i] in memory:
#             del nums[i]
#         else:
#             memory.append(nums[i])
#             i = i+1
        
#     return nums

def find(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None
def find(list, start, target):
    for i in range(start, len(list)):
        if list[i] == target:
            return i
    return None

def my_answer(nums):
    i = 0
    while True:
        print("i = ", str(i), end = " nums = ")
        print(nums)
        if i == len(nums):
            print("break")
            break
        test = find(nums,i+1,nums[i])
        if test is not None:
            del nums[test]
        else:
            i = i+1 
    return nums

def book_answer(nums):
    if len(nums) <= 0:
        return 0
    nums.sort()
    curr = nums[0]
    cnt = 1
    for i in range(1, len(nums)):
        print("nums"+str(nums))
        print("cnt:"+str(cnt) + " curr:"+str(curr) + " i:"+str(i))
        if curr != nums[i]:
            curr = nums[i]
            nums[cnt] = curr
            cnt += 1
            
    return cnt


nums = [0,1,0,2,1,0,2,2,1]
# nums = [0,0,0,1,2,2,2]

# print(my_answer(nums))
print(book_answer(nums))
# print("len:", str(len(nums)))
# print(eliminate_repetition(nums))
