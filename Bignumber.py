# 큰 수의 법칙 

# 공백으로 구분해 입력받음
n, m, k = map(int, input().split()) 
# N개의 수를 공백으로 구분해 입력받음
data = list(map(int, input().split()))

data.sort()
first = data[n - 1] #가장 큰 수
second = data[n - 2] #두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0:
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second
    m -= 1  

print(result)


# m의 크기가 100억 이상일때

n, m, k = map(int, input().split())
data = list(int, input().split())

data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기

print(result)
