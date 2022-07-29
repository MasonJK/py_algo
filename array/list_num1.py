# 주어진 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목푯값을 만들 때, 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하는 프로그램을 작성하라.
# 입력값으로 주어진 배열에는 정확히 하나의 정답이 존재하며, 같은 요소의 값을 중복해서 사용할 수 없다.

nums = [2,7,10,19]
target = 9
answer = []

for i in range(len(nums)):
    if i == len(nums)-1:
        break
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            answer = [i, j]
            break
    if len(answer) != 0:
        break
    
if len(answer) == 0:
    print("no answer available!")
elif len(answer) == 2:
    print("answer is " + str(answer))


        