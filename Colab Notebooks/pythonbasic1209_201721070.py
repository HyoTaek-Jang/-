# -*- coding: utf-8 -*-
"""PythonBasic1209_201721070

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f_6benwmVV6dvjbYhHRcH5PLgDQzmmNZ
"""



"""#정보보호
- 정보를 여러가지 위협으로부터 보호하는 것
- 보호해야할 대상을 자산(asset)이라 함. ex) 컴퓨터 파일, 데이터베이스, 개인정보, 의료정보 etc
- 공격자 : 사람, 컴퓨터, 잠재적으로 해를 끼칠 수 있는 ..
- 취약점 : 정보시스템에 약한 부분.
- 완화 : 취약점을 상쇄하는 보안책/ 안티바이러스, 방화벽(쓸데없는 접속 시도를 애초에 막아버림)
- 완화의 반대 이용(exploit) : 나쁜쪽으로 취약점을 이용하는. 공격자의 의도된 동작을 수행하도록 만들어진 ㄷ데이터 조각
- 위협 : 취약점이 나쁘게 이용되는 것
- 침해 : 손해를 끼치는 것
- 물리적 보안 : 하드웨어를 보호하는 것, 데이터센터 출입보안, 내진설계, 정전대비
- 매개체 : 공격자가 컴퓨터에 접근하기 우해 사용하는 경로나 방법 / ActiveX, email
- 흰색모자 : 화이트해커
- 검정모자 : 블랙해커

#보안의 3가지 특징
- 기밀성 : 정보에 대한 접근이 적절히 제한 되어야만 함.
- 무결성 : 정보가 믿을 수 있다. 데이터 무결성, 소유자 무결성.
- 가용성 : 정보시스템이 정상적으로 사용 가능한 정도.

보안전문가는 보안 보장의 책임이 있음.

사이버 범죄, 아마추어 해커, 컴퓨터 바이러스


사이버 범죄의 행태
- 스푸핑 : 하드웨어의 mac주소, ip주소를 속여 공격하는것
- 릴레이 공격 : 공격의 발워지를 다른 컴퓨터인 것처럼 속이는 것
- 네트워크 스니핑 : 네트워크상의 정보를 엿듣는 행위
- 평문 : 암호화되지 않은 메세지
- 어깨너머 훔쳐보기 : 정보를 뒤에서 몰래 훔쳐보는 기법
- 휴지통 뒤지기 : 휴지통에서 중요 정보를 찾아내는 기법
- 서비스 거부 공격(Dos) : 여러군데에서 동시 다발적으로 접속하여 자원을 부족하게 하여 원래 의도된 용도로 사용하지 못하게 하는 공격
- 스팸 : 불특정 다수에게 보내는 광고
- 쿠키 : 웹사이트 서버에서 사용자 컴퓨터에 설치하는 작은 기록정보 파일, 사용안할수가없음
- 신원도용 : 유출한 개인정보를 이용하여 타인인 것처럼 가장하는 행위

정보보호 방법
1. 인증
- 인증요소
- 1: 주체가 알고 있는 것
- 2: 주체가 소유하고 있는 것
- 3: 주체에 내재하고 있는 것
- 4: 주체가 위치하는 곳

인증이란 "당신이라고 주장하는 그 사람이 정말 당신 맞는가"

인증토큰은 타이머 기능이 있어서 서버와 토큰의 시간을 비교하여 인증과정을 거침.

인가 : 너가 권한이 있어? 를 물어보는 것.

모든 위험의 문제
- 아무리 단단한 보안을 해도 위험이 존재함. 침해 가능성과 피해 정도의 조합 (risk)
ex) 한반도에서 진도 9.5이상 지진이 발생할 확률이 0.000000000001%인데 발생하면 100조 피해.

정보보호에 좋은 법
1. 암호화
2. 방화벽
3. 안티바이러스 소프트웨어
4. SW 업데이트
5. 백업
6. 로그 파일


암호화
- 양방향 암호화 : 암호화와 복호화(암호화를 평문으로)가능
- 단방향 암호화 : 오직 암호화만 가능.

단방향 예시. 패스워드를 만들때 암호화해서 넣고, 인증할때 내 입력값도 암호화해서 db랑 비교하는거 유출돼도 안전하게. 해쉬가 두 개가 있어야함.

공개키 암호
- 2개의 키를 사용하는 양방향 암호
- 개인키 : 오직 당사자만 암
- 공개키 : 모두가 암
서로 열수있음.

공개키 암호를 이용하는 두 가지 방법
- 개인키로 암호화 - 공개키로 복호화는 데이터 무결성 보전(내가 보낸게 맞아!)이 목적이다.
- 공개키로 암호화 - 개인키로 복호화는 데이터 암호화가 목적이다.

디지털 서명
- 평문을 해쉬하여서, 제인 개인키로 암호화하고, 요세 공개키로 암호화함.
- 암호문을 요세 개인키로 복호화하고 서명은 제인 공개키로 복호화함!

공인 인증서

인증기관

방화벽
- 일부 네트워크 트래픽을 허용하거나 차단하도록 정의
- 하드웨어 장치나 컴퓨터 시스템 내의 소프트웨어 방화벽이 있음.
- 접근 제어 목록 : 블랙 리스트 : 공격자의 IP목록. 스팸필터 : 사용자의 행위를 기반으로 필터가 설정
- 거짓 양성 : 허용되어야 할 메시지를 차단하는 경우 발생. 중요한 메시지가 스팸에 있을 때

비트 서명 : 바이러스가 갖고있는 특정한 비트열.


좋은 전력
- 가장 취약한 연결부(와이파이, 사용자) 보호
- 공격 외관 축소하기
- 철저하게 방어
- 피해가 퍼지지 않게 구획으로 나누기
- 쉽게 신뢰하지 않기
- 믿을만한 오픈 SW 잘 사용 not 무료 sw


호스츠 파일을 점검해야함. 호스츠에 아무것도 없어야함.


"""