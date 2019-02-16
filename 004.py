# 004.py
# 0부터 10,000까지 8이라는 숫자는 총 몇번 등장하는가?

print(str(list(range(1,10000))).count('8'))
# .count 나 .max .min 등은 내장메서드이기 때문에 최적화가 되어 있다.
# 그래서 바로 짜는 것보다 더 최적화가 되어 있기 때문에 더 빠르다.
# dir() 쳐서 나오는 내장메서드들은 20% 이상 알아야(외워야) 하고 
# 모두 쓸 줄 알아야 한다. 