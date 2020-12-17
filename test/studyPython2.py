# 기본매개변수, 키워드 매개변수
# 기본 매개변수 : 함수 호출시, 매개변수가 없으면 기본적을 할당. 초기값 개념
# 키워드 매개변수 : 매개변수 순서 없이 함수 호출시 키워드로 전달.
def func(a, b=5, c=3):
    print(a, b, c)


func(1, 2)
func(2, 3)
func(10, b=20)


# 기본매개변수는 뒤에 놔야함.

# VARIABLE ARGUMENTS 매개변수의 갯수를 모를 때 활용. 몇개가 오든 상관없을때
def total(initial=5, *numbers, **keywords):  # numvers는 tutple, keywords 딕셔너리 자료구조
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


print(total(10, 1, 2, 3, a=10, b=20))


# return 자기가 계산한 값을 돌려줌. 경우에 따라 같은 함순데 인트도 보내고 스트링도 보내고 함ㅋㅋㅋ 리턴타입이 달라도 ㄱㅊ

def maxium(x, y):
    '''
    doc String
    :param x:
    :param y:
    :return:
    '''
    if x > y:
        return x
    elif x < y:
        pass
    else:
        return ('동일')


print(maxium(5, 7))
help(maxium)  # help를 통해 나오는거


# 리턴값이 튜플도 됨. (x,y) 같은거로 ㅇㅇ 리턴안하고 pass하면 None이 뜸. 값이없음을 이해함. 파이썬 예약어 null같은 느낌.

def sumto(N):
    '''
    1부터 N까지 더해줌
    '''
    s = 0
    i = 1
    while i <= 10:
        s += i
        i += 1
    return s


print('sum of integers from 1 to {} is {}'.format(10, sumto(10)))


def sumto2(N, step=1, start=1):
    '''
    1부터 N까지 더해줌
    '''
    s = 0
    i = start
    while i <= N:
        s += i
        i += step
    return s


print('sum of integers from i to {} is {}'.format(10, sumto2(10)))
print('sum of integers from i to {} is {}'.format(10, sumto2(100, 2, 2)))


def fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N < 0:
        print('Error')
        return 0

    bf1 = 0
    bf2 = 1
    i = 2
    while (i <= N):
        fibo = bf1 + bf2
        bf1 = bf2
        bf2 = fibo
        i += 1

    return fibo


def fibonacci2(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N < 0:
        print('Error')
        return 0

    return fibonacci2(N - 2) + fibonacci2(N - 1)


print(fibonacci2(10))
print(fibonacci(4))


def selectionSort(A):
    i = 0
    N = len(A)
    while i < N - 1:
        j = i + 1
        minj = i
        while j < N:
            if A[minj] > A[j]:
                minj = j;
            j += 1
        temp = A[minj]
        A[minj] = A[i]
        A[i] = temp
        i += 1
    return A


c = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(selectionSort(c))
