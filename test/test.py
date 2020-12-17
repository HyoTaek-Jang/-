# 프린팅

print("{} 입니다".format("taek"))

print("{0} 포멧팅 {2}".format("0번", "1번", '2번'))

print("{0} 포멧팅 {NUM}".format("0번", NUM="123"))

name = "택"
age = 23

print(name + "is" +str(age) + " years old")
# int 자동 캐스팅 안됨.

print("{num:.3f}".format(num = 3.141592))
# :.f 플로트형식 소수점 세자리.

print("{: ^12}".format("Taek"))
print("{:ㅇ>12}".format("Taek"))
print("{:ㅇ>4}\n\n엔터".format("Taek"))
# :(채울 글자)(^,> 오른쪽 정렬,< 왼쪽 정렬)num(총 몇칸)
# 만약 적으면 그대로 출력하는 듯
# \n 이스케이프 문자