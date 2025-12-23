# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

answer = OrderedDict()

n = int(input())
for i in range(n):
    x = input()
    if(x in answer.keys()):
        answer[x]+=1
    else:
        answer[x]=1

print(len(answer.keys()))
for i in answer:
    print(answer[i], end=" ")