# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    x = input().split()
    if(len(x)>1):
        op, num = x[0], int(x[1])
    else:
        op = x[0]
    if(op=="append"):
        d.append(num)
    elif(op=="pop"):
        d.pop()
    elif(op=="popleft"):
        d.popleft()
    elif(op=="appendleft"):
        d.appendleft(num)
    else:
        print("Invalid input")
for i in d:
    print(i, end=" ")