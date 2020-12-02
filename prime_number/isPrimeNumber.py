import timeit
"""
창의소프트웨어입문 파이썬 개인과제 1 201721070 장효택

알고리즘을 코드로 구현하고 timeit을 활용하여 시간을 측정하여 성능 체크를 했다.

isPrimeNumber : num을 2~num^(1/2)까지 나눠서 나눠 떨어지지 않으면 소수다. 소수인 99999989을 넣었을 때, 0.00435초
isPrimeNumber_1 : num을 2부터 num까지 나눠서 나눠 떨어지지 않으면 소수다. 소수인 99999989을 넣었을 때, 12.00103초
isPrimeNumber_2 : 에라토스테네스의 체를 사용하여 소수를 체크했다. 소수인 99999989을 넣었을 때, 22.3828초

위의 결과를 바탕으로 가장 좋은 성능을 보인 첫 번째 알고리즘을 사용하여 isPrimeNumber을 구현했다.
"""

def isPrimeNumber(num):
    if (num <= 1):
        return False
    divisor = 2
    while (divisor < int((num ** 0.5) + 1)):
        if num % divisor == 0:
            return False
        divisor += 1
    return True

"""
def isPrimeNumber_1(num):
    if num <= 1:
        return False
    divisor = num - 1

    while divisor > 1:
        if num % divisor == 0:
            return False
        divisor -= 1
    return True

def isPrimeNumber_2(num):
    checkBoard = [True] * num

    if (num <= 1):
        return False

    for i in range(2, int((num ** 0.5) + 1)):
        if checkBoard[i] == True:
            for j in range(i + i, num + 1, i):
                if j == num:
                    return False
                checkBoard[j] = False
    return True

start_time = timeit.default_timer()
isPrime_1 = isPrimeNumber(99999989)
terminate_time = timeit.default_timer()
time = terminate_time - start_time

print(isPrime_1, time)

"""