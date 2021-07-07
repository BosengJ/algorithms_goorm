# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

a,b = map(int,input().split())

bin_a = bin(a)[2:]

#Right shift
if a < 0:
	r_shift = ('1' * b) + bin_a[:-b]
else:
	r_shift = ('0' * b) + bin_a[:-b]
	
#Left shift
l_shift = bin_a[b:] + ('0' * b)

print(r_shift)
print(l_shift)