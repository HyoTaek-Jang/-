# 프린팅

print("{} 입니다".format("taek"))

print("{0} 포멧팅 {2}".format("0번", "1번", '2번'))

print("{0} 포멧팅 {NUM}".format("0번", NUM="123"))

name = "택"
age = 23

print(name + "is" + str(age) + " years old")
# int 자동 캐스팅 안됨.

print("{num:.3f}".format(num=3.141592))
# :.f 플로트형식 소수점 세자리.

print("{: ^12}".format("Taek"))
print("{:ㅇ>12}".format("Taek"))
print("{:ㅇ>4}\n\n엔터".format("Taek"))
# :(채울 글자)(^,> 오른쪽 정렬,< 왼쪽 정렬)num(총 몇칸)
# 만약 적으면 그대로 출력하는 듯
# \n 이스케이프 문자

a = 5
b = "123"
c = 4.56
print(a, b, c)
# 따로 Type을 명시하지 않음.

a = 7
if a == 3:
    print("a is 3")
elif a == 7:
    print("a is 7")
else:
    print("i dont know")
# 코드의 분리를 {}가 아닌 들여쓰기로 함.

c = a * b  # 문자열 b를 a번 만큼 반복
print(c)

c = b + str(a)  # 문자열 + 인티저 안됨 자동형변환 놉
print(c)

a = a - 10.5  # 정수 - 플로트는 되는듯
print(a)

a = 3
b = 2
a = a ** b  # a^b, 부동소수점 거듭제곱 연산도 가능
print(a)

print(13 / 3)  # 부동소수점으로 나옴
print(int(13 / 3))  # 인트로 바꿈
print(13 % 3)
print(3 << 4)  # 3을 비트형식으로 왼쪽으로 4번 옮김 곱셈 1칸당2, 여기선 4니까 16곱한거
print(4 >> 1)  # 나눗셈

print("")

print(5 % 3)  # 비트로 표현해서 둘다 1이면 1
print(3 | 3)  # 하나라도 1이면 1
print(5 ^ 3)  # 값이 다르면 1
print(~-5)  # 반전. 단양 연산자. 부호를 결정하는 비트까지 뒤집음 -(x+1)이 나옴

print(bin(5))  # 이렇게하면 됨. 0b는 바이너리임을 알리는 것
print('{0:b}'.format(6))  # :b를 통해 바이너리다~

print(3 == 3 and "abc" == str.lower("ABc"))
print(3 == 3 and "abc" == "ABc")

print(3 == 3 or "abc" == str.lower("ABc"))
print(3 == 3 or "abc" == "ABc")
# && ||가 아님.

a = 4
a += 2
print(a)

# if문
# 조건문이 true이면 블럭을 실행, 의사코드나 플로우차트ㅔ서 조건 분기 역할을 한다.
number = 11
inputNum = int(input('Enter int : '))  # input은 문자열을 반환하고 int로 형변환을하여 inputNum은 인트를 받음.
if (number == inputNum):  # :은 함수,조건문,루프의 시작을 :으로 표현함. 새로운 명령블럭의 시작 ㅇㅇ, 괄호쳐도 되고 안해도 되는듯
    print('if 1번')  # 꼭 인덴테이션 해줘야해
    print('if 2번')
elif number < inputNum:  # else if = elif 이것도 :쳐줘야함, else하고 그 안에서 if해도 되는데 굳이? 복잡하게?
    print('number가 작아')
else:
    print('number가 커')
print('done')  # 항상 실행

running = True
while running:
    print('펄스까지 계속실행')
    running = False
else:
    print('while끝나면 1번 실행됨')  # 쓸수는있는데 없어도 됨. 거의 안씀

    # for loop
    # 나열된 값들에 대해 순차적으로 처리하고자 할 때 사용. for는 in이랑 거의 함께 쓰임.

    for i in range(1, 5):  # i는 1~4까지 돔.
        print(i)
    else:
        print('for문 끝')

    # range(1,5,2) -> 1부터 5까지 2씩 증가한다. 맨뒤에 안써주면 1로 디폴트 값

    sum = 0
    for i in range(1, 11):
        sum += i
    print('loop is over', sum)
    # range는 객체임. range(1,5)를 배열로 바꾸면 [1,2,3,4] 나옴.

    for i in [1, 2, 3, 4]:
        sum += i
    print(sum)

    compareValue = 'quit'

    while True:
        inputValue = input('입력해라 요놈아')
        print('와일문입니다')
        if len(compareValue) > len(inputValue):
            print('4글자보다 작다 요놈아')
            continue
        elif len(inputValue) > 4:
            print('4보다 크다ㅏㅏ')
            continue
        elif compareValue == inputValue:
            break
        else:
            print("길이는 같다")
        print("와일문 마지막 부분")
    print('와일문 끝')


# 함수는 재사용하겠다! 코드를 재사용, 매개변수에 따라 다양한 결과 출력.
def say_hello():  # def 이름(매개변수):    def는 함수 외 class를 정의할떄도 사용함
    print('함수입니다용')


say_hello()


# 매개변수는 다양한 기능을 구현하기 위해. 한 함수로!
def print_max(a, b):
    print('a는', a, 'b는', b)


print_max(4, 3)

x = 3;
y = 1  # ;는 한 라인에서 두 익스프레션을 구분할 때.
print_max(x, y)

# 지역변수와 글로벌변수. 변수의 범위
# 블록안의 변수는 지역변수고, 블록 안에서만 인식됨.
# 글로벌은 블록 밖에 선언된 변수를 참조함.
x = 60
y = 10


def func(a):
    print('x :', a)  # 매개변수로 받은 외부x.
    print('y :', y)  # 외부 y변수
    a = 3
    global x  # 외부 x 주소를 받아서 이제 x를 수정하면 외부 x도 수정됨, 외부에 값이 없으면 에러뜸.
    print('x :', x)  # 윗라인 x=3


func(x)


