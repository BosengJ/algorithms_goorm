'''리그 경기 횟수 구하기

리그에 속해있는 팀의 수 n이 주어지고 각 팀은 자신을 제외한 모든 팀과 한 경기 씩 치루어 순위를 가리는 스포츠 리그전에서 치루어지는 경기의 수를 구하는 프로그램을 작성하십시오.

2팀이면 1경기, 3팀이면 3경기, 4팀이면 6경기가 치루어 집니다. 


입력

리그에 참여하는 팀의 수

출력

리그에서 치루어 지는 경기의 수'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = raw_input()
# print "Hello Goorm! Your input is ", user_input

n = int(input())

answer = 0
for i in range(n-1):
	for j in range(i+1,n):
		answer += 1
		
print(answer)