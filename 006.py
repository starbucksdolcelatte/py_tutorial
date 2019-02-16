# 006.py
# while, for 

'''
while True:
    x = input('##')
    if x == 'exit':
        break
    else:
        break
'''

# 1부터 100까지의 짝수를 더하는 것
print([x for x in range(0,101) if x%2 == 0])
print(sum([x for x in range(0,101) if x%2 == 0]))

# 구구단 출력
print([x for x in range(1,10)])
print([['{}*{}={}'.format(x, y, x*y)] for x in range(2,10) for y in range(1,10)])


a = 100
b = a 
c = b

print(id(a)) # a가 가리키는 곳의 주소값 : 100이라는 값이 들어있는 곳을 가리키고 있다.
print(id(b)) # b가 가리키는 곳의 주소값
print(id(c)) # c가 가리키는 곳의 주소값
