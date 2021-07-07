'''비트연산 기본 2

비트 연산의 꽃이라고 할 수 있는 시프트(Shift) 연산에 대해 배우고 실습하는 문제입니다. 시프트(Shift)의 결과값이 출력되는 프로그램을 작성하십시오.

비트 값(열)을 지시한 만큼 왼쪽이나 오른쪽으로 이동시키는 연산자 입니다. 많은 상황에서 효율적으로 사용될 수 있으므로 잘 익혀두시길 바랍니다.

1. Right Shift ( >> )

오른쪽으로 특정 비트 수 만큼 이동하고 빈자리는 양수 일때는 0, 음수 일때는 1로 채운다.

2. Left Shift ( << )

왼쪽으로 특정 비트 수 만큼 이동하고 빈자리는 0으로 채운다.



입력

두개의 수 a, b

출력

첫 줄에 a >> b의 결과

다음 줄에 a << b의 결과'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

a,b = map(int,input().split())

# Right shift
if a > 0:
	right_2 = '0b' + ('0'*b) + bin(a)[2:-b]
	right_10 = int(right_2,2)
else:
	right_2 = '0b' + ('1'*b) + bin(a)[2:-b]
	right_10 = int(right_2,2)
	
# Left shift
left_2 = bin(a) + ('0'*b)
left_10 = int(left_2,2)

print(right_10)
print(left_10)



