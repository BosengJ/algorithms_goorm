'''태민이의 취미

태민이는 주사위를 수집하는 취미를 가지고 있습니다. 주사위의 모양과 색깔은 각기 다르며, 크기 또한 다릅니다. 태민이는 지금까지 모은 N개의 주사위가 너무 난잡하게 보관해놓고 있어서 정리를 결심했습니다. 그래서 우선 N개의 주사위를 크기 순서대로 정리해보려고 마음 먹었습니다.

그렇게 주사위를 순서대로 정렬시켜보니 각 변의 길이가 1부터 N까지 모두 있는 것을 알게되었습니다. 이 사실이 매우 신기했던 태민이는 이 주사위들의 부피의 합은 어떻게 될지 궁금해졌습니다. 태민이가 현재 가지고 있는 모든 주사위의 부피의 합은 얼마일까요? 태민이의 궁금증을 풀어주세요!


입력

첫 줄에 정수 N이 주어집니다. (단, )


출력

변의 길이가 1부터 N까지인 주사위들의 부피의 합을 출력합니다.

이때, 수가 너무 커질 수 있으므로 1000000007로 나눈 나머지를 출력합니다.'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

n = 8764891


volume = 0
for n in range(1,n+1):
	volume += n ** 3

print(int(volume% 1000000007))


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)

n = int(input())

sum_volume = int(n * (n+1) / 2)
sum_volume *= sum_volume

answer = sum_volume % 1000000007
print(answer)