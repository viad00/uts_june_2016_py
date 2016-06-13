import sys

problem_name = str('friends')
sys.stdin = open(problem_name + ".in", "r")
sys.stdout = open(problem_name+".out", "w")
friends = int(input())
# В полном графе n(n-1)/2 рёбер (из Википедии)
nan = friends * 2  # n^2-n = nan
out = -1
for n in range(friends):
    if n ** 2 - n == nan:
        out = n
        break
if out != -1:
    print(out)
elif friends == 1:
    print(2)
else:
    print('NO')
