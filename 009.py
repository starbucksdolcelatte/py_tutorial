# tuple
t = (100, 200, 300, 400)

'''
1. tuple 안에는 다른 object 들이 들어갈 수 있다.
2. 값(주소값)을 변화시킬 수 없습니다.
3. 순서가 있습니다.
'''

l = ['hello world']
t1 = (100, 200, 300, l) # t1에서 l 을 가리키고 있다는 것은 변화하지 X
# l의 내용은 바꿀 수 있다. 그러나 이런 식으로 코딩하면 보안상 문제 발생.
# 그렇게 하지 말아라.

