print('Все проекты в папках.')
'''
пример чтения из файла
'''

import sys

sys.stdin = open("something.in", "r")
sys.stdout = open("something.out", "w")
a, b = map(int, input().split())
c = int(input())
