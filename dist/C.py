import sys
problem_name = str('dolbak')
sys.stdin = open(problem_name + ".in", "r")
sys.stdout = open(problem_name+".out", "w")
# Чтение и сортировка
len_have = int(input())
have = input().split()
for i in range(len(have)):
    have[i] = int(have[i])
len_beat = int(input())
beat = input().split()
for i in range(len(beat)):
    beat[i] = int(beat[i])
# Программа
# Флаг на -1
flag = 0
# Заводим список действий
todo = []
for card_to_beat in range(len(beat)):
    # Ищем подходящюю карту
    card_curr = -1
    for card_now in range(len(have)):
        if have[card_now] > beat[card_to_beat]:
            if card_curr == -1:
                card_curr = card_now
            elif have[card_curr] > beat[card_to_beat]:
                card_curr = card_now
    # Используем
    have[card_curr] = 0
    todo.append(card_curr)
    # Флаг на -1
    if card_curr == -1:
        flag = 1
for i in range(len(todo)):
    todo[i] = todo[i]+1
if flag > 0:
    print(-1)
else:
    print(*todo)