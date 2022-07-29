# 초기화
# py_list_zeros1d = [0 for i in range(10)]
# py_list_zeros2d = [[0 for i in range(10)] for j in range(10)]

# print("1d")
# print(py_list_zeros1d)
# print("2d")
# print(py_list_zeros2d)

####

# append, extend
# apped는 요소로 추가하는 것이고, extend는 확장시키는 것이다.
# 이들은 새로운 객체를 만드는 것은 아니고, 기존 객체에 하는 짓이다.
# list = [0 for i in range(3)]
# list.append([1,1,1])
# list.extend([1,1,1])

# print(list)

###

# insert, remove, clear, del
# insert는 첫 인자에 위치, 두 번째 인자에 값을 준다.
# remove는 값을 인자로 주면 값을 가지고 있는 가장 앞선 인덱스의 요소가 삭제된다. 만약 요소가 없으면 error 발생
# clear는 모든 요소 삭제.
# del을 이용해서 인덱스를 활용한 삭제
# py_list = [i+1 for i in range(5)]
# py_list.insert(5,6)
# py_list.remove(3)
# del py_list[1]
# py_list.clear()

# print(py_list)

###

# 슬라이싱
# 1개 쓰면 시작부터 끝 전까지
# 2개 쓰면 시작부터 끝 전까지 step만큼 뛰어서
# 2개 쓸 때 꿀팁은 step을 음수로 가져오면 역순으로 가져올 수 있다는 점.
# --> 이것은 range도 마찬가지.
# py_list = [i+1 for i in range(5)]
# print(py_list)
# print(py_list[::-1])


