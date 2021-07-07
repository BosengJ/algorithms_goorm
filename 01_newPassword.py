'''https://level.goorm.io/exam/49090/%EC%83%88%EB%A1%9C%EC%9A%B4-%EC%95%94%ED%98%B8%ED%99%94/quiz/1

새로운 암호화

예진이는 암호학 수업을 들으면서 다양한 암호화 기법들을 익혔습니다. 그러던 도중 자신만의 암호화 기법을 만들어보고 싶은 생각이 들었습니다. 그리고 이러한 암호화 방법에 대해 생각해보았습니다.

key: 임의의 정수 A, B (A ≤ B)
result: A, A+1, A+2, ..., B를 모두 xor한 값
예를 들어 key로 2와 4를 정했다면 2 xor 3 xor 4 = 5가 됩니다. 본디 암호화란 복호화가 가능하여 결과값을 통해 key를 알아낼 수 있어야 하지만 아직 그런 걸 고려할 수 있을 정도로 예진이는 많이 배우지 못했습니다.

일단 이렇게 만들어진 예진이의 암호화 방법에서 key로 사용되는 정수 A와 B를 알 때, 암호화한 값이 무엇인지 출력하는 프로그램을 작성해주세요.



입력
첫째 줄에 정수 A와 B가 공백으로 구분되어 주어집니다.

(단, )



출력
A부터 B 사이의 모든 정수를 xor했을 때 결과값을 출력합니다.'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

A = int(user_input.split(' ')[0])
B = int(user_input.split(' ')[1])

answer = 0
for n in range(A,B+1):
	if n == A:
		answer += n
	else:
		answer = answer ^ n
print(answer)