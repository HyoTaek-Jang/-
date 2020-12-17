'''
#자료구조
자료구조는 데이터를 담는 그릇의 형태

리스트, 튜플, 딕셔너리, 집합 총 4가지 기본 자료구조가 있음

##리스트
- 순서대로 정리된 하옴ㄱ들을 담고 있는 목록 형태의 자료구조
- 타입이 섞여있어도 됨.
- 항목을 대괄호로 묶어서 사용
- 접근은 [num]으로 함
'''
shoplist = ['apple', 'mango', 'banana']
print(len(shoplist))

for i in shoplist:
    print(i, end=" ")  # end쓰면 뉴라인 안뜨고 걍 뒤로 이어서 적음

print("\n", shoplist)

shoplist.sort() #알파벳 순서로
print(shoplist)
print(shoplist[1])
del shoplist[0]  # 0번쨰 아이템 지움
print(shoplist)
'''
#튜플
- 리스트랑 비슷하지만 수정 불가임
- () 괄호로 묶음
'''
zoo = ('python', 'rabbbit', 'monkey')
print(len(zoo))
new_zoo = 'camel', zoo
print(len(zoo))
# 왜 갯수가 4개가 아니냐 zoo는 저 튜플이 한개로 치는거임.
print(new_zoo[1][1])
# 리스트도 append로 똑같이 할 수 있음. 괄호를 안써도 되는데 써주는게 좋음
# 하나짜리 튜플을 마지막에 ,를 붙여줘야함
# 못바꾸지만 성능이 좋음 결과값 넣는거로 자주씀
# a, b = b, a -> 서로 값 바뀜
'''
#Dictionary
- 키와 벨류를 갖는 자료구조. 한 데이터 내에 속성을 ㅇㅇ
- 키는 유일해야하고 문자열 숫자등으 ㅣ정적객체이어야 한다.
- 키 밸류 쌍은 ,로 구분한다.
- 중괄호로 {} 표시한다.
- 조회는 []에 키값으로 검색한다.
'''
ab = {'효택' : '굿',
      '수지' : '구웃'}
print(ab)
print(len(ab))
print(ab['수지'])
print(ab.keys())

ab['택'] = '구구구구굿' #추가

for key, a in ab.items():
  print(key, a)

print(ab.items())
print(ab.values())

if '택' in ab:
  print('x택이따')
for key in ab:
  print(key, ab[key])

#자료구조에 다른 자료구조가 들어갈 수 있음 조합 가능


#열거형 자료구조에 대한 연산 방법
# 리스트 튜블 무자열 등을 열거형 데이터라 함
#인덱싱 음수 가능.

print('apple' in shoplist) # in, not in
# 문자열은 한칸이 인덱싱 1개임. 공백도 ㅇㅇ



# slicing on a list
shoplist = ['apple','mango','banana'] #2-4번째꺼 전까지
print(shoplist[1:3]) #2번째 부터 3인덱스 만나기 전까지 
print(shoplist[1:]) #2번쨰부터 ㄱㄱ
print(shoplist[1:-1]) # 2~ 마지막까지 전까지

#slicing with step
# shoplist[::2] 2칸씩 뛰어넘음

#집합
'''
- 집합 연산을 할 수 있는 자료구조
- 중복된 값을 무시하고 유니크 벨류만 기록됨.
'''


#con = country.copy()
#셋은 추가할때 add로 함 어디에 들가든 유니크해서 ㄱㅊ
#issuperset(~) ~를 갖고있냐
#con.remove(~)
#con & country -> con.intersection(~)
# con | country -> con.union(~)

# 참조. 열거형 변수를 어사인하면 그 값을 갖는게 아니라 메모리 위치를 주는거임.
# 값을 복사하려면 mylist = shoplist[:] 이거 값만 같은거임 주소를 공유하는게 아니라.
print(shoplist[::2]) #처음 뜨고 두칸씩 넘어감.)


