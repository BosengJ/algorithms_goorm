'''거울 단어

거울 단어는 단어를 실제로 거울에 비춰봤을 때 원래 단어와 똑같은 단어를 의미합니다. 예를 들어, "poq"나 "bidbid"는 거울 단어입니다. 하지만 "tomato"나 "apple"은 거울 단어가 아닙니다. 한 알파벳을 거울에 비춰봤을 때 어떤 알파벳으로 보이는지 표로 정리하면 다음과 같습니다.


b	d
i	i
l	l
m	m
n	n
o	o
p	q
s	z
u	u
v	v
w	w
x	x
표에 없는 알파벳은 거울에 비춰봤을 때 쌍을 이루는 알파벳이 없음을 의미합니다. 입력으로 알파벳 소문자로만 이루어진 N개의 단어가 주어질 때, 각 단어가 거울 단어인지 아닌지 판별하는 프로그램을 작성해주세요.


입력

첫째 줄에 테스트케이스의 수 T가 주어집니다. (단, )

이후 T줄에 걸쳐 알파벳 소문자로만 이루어진 단어가 입력으로 주어집니다. 이때 각 단어의 길이는 1 이상 100 이하입니다.


출력
각 케이스별로 거울 단어라면 "Mirror"를, 아니면 "Normal"을 출력합니다.'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)
n = int(input())
n_list = []
for i in range(n):
	n_list.append(input())
	
mirror_dict = {'b':'d','d':'b','i':'i','l':'l','m':'m','n':'n','o':'o',
'p':'q','q':'p','s':'z','z':'s','u':'u','v':'v','w':'w','x':'x'}

for word in n_list:
	tmp = list(word)
	
	mirror_word = ''
	for ch in tmp[::-1]:
		if ch in mirror_dict:
			mirror_word += mirror_dict[ch]
		else:
			break
	if mirror_word == word:
		print('Mirror')
	else:
		print('Normal')
	
