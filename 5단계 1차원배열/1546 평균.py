import sys

N = int(input())
score = sys.stdin.readline().split()
num_score = []

for i in range(len(score)):
    num_score.append(int(score[i]))

revise_score = []

hap = 0
for i in range(N):
    revise_score.append(num_score[i]/max(num_score)*100)
    hap += revise_score[i]


print(hap/N)

