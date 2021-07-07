'''369 게임

여름을 맞아 친구들과 여행을 간 구름이는 369게임을 하게 됐다.

369게임은 여러명이 둘러앉아서 숫자를 하나씩 돌아가며 말하다가 숫자에 3,6,9가 포함된 숫자가 되면 박수를 치는 게임이다.

(이 때, 해당 숫자에 3,6,9가 여러개이면 박수를 개수만큼 쳐야한다. 예를 들어 33, 36의 경우 박수를 두 번 쳐야 한다)

게임이 끝난 숫자 N이 주어졌을 때, N 이전까지 박수를 친 횟수를 구하여라.'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

n = int(input())
clap = ['3','6','9']
answer = 0
for num in range(1,n+1):
	num_str = list(str(num))
	for n in num_str:
		if n in clap:
			answer += 1
print(answer)