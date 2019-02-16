# list
# 여기서 배우지 않은 이야기는 책에 더 자세히 나와 있다.
# 두꺼운책보다는 얇은 책 여러권을 보기를 추천
# 두꺼운책은 내 실력 도약이 필요하다 싶을때 본다.

l = [100, 200, 300, 400]

'''
1. list 안에는 다른 object 들이 들어갈 수 없다.
2. 값을 변화시킬 수 있습니다.
3. 순서가 있습니다.
'''

print(l[3])
print(l[:4:2])
#print(l[start:stop:step])

print(l)
print(type(l))
print(dir(l))

l.append(500)
print(l)

c = l.copy()
print(c)
print(l.count(100))

l.extend([100, 200, 300])
print(l.index(500))

l.insert(3, 100000) # 3번째 인덱스에 100000을 넣어준다.
print(l)

l.pop()
print(l)

l.remove(100) # 처음 만나는 100만 지운다. 다 지우려면.count(100)번 만큼 반복하면서 다 지운다.
print(l)

l.reverse() # 얘는 리스트 내장함수라 리스트를 직접 만든다.
print(l)
print(reversed(l)) # 리스트를 직접 안 만지고 프린트만..

l.sort() # 리스트를 직접 만진다.
print(l)
print(sorted(l)) # 리스트 직접 조작 x