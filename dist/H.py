import sys

problem_name = str('internet')
sys.stdin = open(problem_name + ".in", "r")
# sys.stdout = open(problem_name+".out", "w")
n = int(input())
inst = []
lastpos = 9999999999
lastpower = 0
success = True
for i in range(n):
    curpos, curpower = map(int, input().split())
    if lastpos + lastpower < curpos:
        success = False
        break
    lastpos = curpos
    lastpower = curpower
if success:
    print("YES")
else:
    print("NO")
