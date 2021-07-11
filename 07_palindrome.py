# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = raw_input()
# print "Hello Goorm! Your input is ", user_input

# word_list = ['abba','summuus','xabba','xabbay','comcom','comwwmoc','comwwtmoc']

n = int(input())
word_list = []
for i in range(n):
	word_list.append(input())
	
# def pseudoPD(word):
# 	for i in range(len(word)):
# 		del_word = word[:i] + word[(i+1):]
# 		reversed_del_word = del_word[::-1]
# 		if del_word == reversed_del_word:
# 			return True
# 	return False

def checkString(s):
	for i in range(len(s)//2):
		if s[i] != s[-i-1]:
			return False, i
	return True, i

def pseudoPD(word):
	TF, idx = checkString(word)
	s1 = word[:idx] + word[idx+1:]
	s2 = word[:len(word)-idx-1] + word[len(word)-idx:]
	TF_s1, _ = checkString(s1)
	TF_s2, _ = checkString(s2)
	if (TF_s1 == True) or (TF_s2 == True):
		return True
	return False

for word in word_list:
	reversed_word = word[::-1]
	if reversed_word == word:
		print(0)
	elif pseudoPD(word) == True:
		print(1)
	else:
		print(2)
