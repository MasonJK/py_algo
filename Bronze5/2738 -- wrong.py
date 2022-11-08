# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
import numpy as np

def makeMat():
    mat = np.array()
    mat.append(np.array(map(int, input().split())))
    mat.append(np.array(map(int, input().split())))
    mat.append(np.array(map(int, input().split())))
    return mat   

N, M = map(int, input().split())
A = makeMat()
B = makeMat()

print(A+B)