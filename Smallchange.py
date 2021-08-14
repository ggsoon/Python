#거스름돈을 구하는 알고리즘
from random import randint 
from array import array
import time

Start_time = time.time()

n = randint(10, 5000)
coin_type = [500, 100, 50, 10]
count = 0
print(n)

for coin in coin_type:
    count += n // coin # 해당 화폐로 거스를 줄 수있는 동전의 개수 세기
    n %= coin # 헤당 화폐를 마이너스함

print(count)    

End_time = time.time()

print("성능 : ", Start_time - End_time)