# class
class Car(object):
    maxpeople = 5
    maxspeed = 300
    def start(self):
        print('차가 출발하였습니다. ')
    def stop(self):
        print('차가 멈췄습니다.')

    
        
k3 = Car()
k3.start()
print(type(k3))

# 상속
print(dir(k3))
# object 라는 클래스를 상속받은 Car 클래스
# 따라서 우리가 정의하지 않은 많은 메서드들이 있다.
# __class__, __init__ 등등

# Car 클래스를 상속받은 HybridCar 클래스
class HybridCar(Car):
    battery = 100
    batteryKM = 300
    

hyk3 = HybridCar()
print(hyk3.maxpeople)