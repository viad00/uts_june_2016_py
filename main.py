print('Все проекты в папках.')
'''
пример чтения из файла
'''

import sys
problem_name = str('smthg')
sys.stdin = open(problem_name + ".in", "r")
sys.stdout = open(problem_name+".out", "w")
a, b = map(int, input().split())
c = int(input())
