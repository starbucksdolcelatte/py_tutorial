a = True
b = False
print(int(a or b))

sumi = 0
for i in range(1, 1001):
    # 15의 배수
    if i % 3 == 0 and i % 5 == 0:
        sumi += 1
print(sumi)