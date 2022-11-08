array3 = [4.1,3.0,2.8,2.9,3.1,3.6,3.7,4.0]
array2 = [60,55,75,67,49,63,58,61]
array1 = [170,165,174,169,155,172,166,168]

def getcov(arr1, arr2, m1, m2):
    tot = 0
    for i in range(len(arr1)-1):
        tot += (arr1[i] - m1) * (arr2[i] - m2)
    ret = tot/len(arr1)
    print('total = '+str(tot))
    print('cov: '+str(ret))
    print()
    return ret


def getmean(arr):
    meantot = 0
    for i in arr:
        meantot+=i
    print('mean: ' + str(meantot/len(arr)))
    return meantot/len(arr)

mean1 = getmean(array1)
mean2 = getmean(array2)
mean3 = getmean(array3)

print()
getcov(array1,array2,mean1, mean2)
getcov(array1,array3,mean1, mean3)
getcov(array2,array3,mean2, mean3)