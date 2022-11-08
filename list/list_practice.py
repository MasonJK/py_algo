nums = [2,7,10,19]
target = 9

def AddTwoSums():
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
            
print(AddTwoSums())

def AddTwoSumsHash():
    hash = {}
    for i in range(len(nums)):
        value = target-nums[i]
       
        if (hash.get(value) is not None) and (hash[value] != i):
            return sorted([i, hash[value]])
        
        hash[nums[i]] = i
    
    return [-1,-1]

print(AddTwoSumsHash())
    