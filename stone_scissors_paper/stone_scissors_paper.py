import random

janken = ['グー', 'チョキ', 'パー']

def result(player, cpu):
    # 勝ち＝1　負け＝２　あいこ＝３
    if player == 'グー' and cpu == 'チョキ':
        return 1
    elif player == 'グー' and cpu == 'パー':
        return 2

    if player == 'パー' and cpu == 'グー':
        return 1
    elif player == 'パー' and cpu == 'チョキ':
        return 2

    if player == 'チョキ' and cpu == 'パー':
        return 1
    elif player == 'チョキ' and cpu == 'グー':
        return 2
    else:
        return 3

def game():
    print('何を出しますか？ >>> ', end= '')
    player = input()

    while player not in janken:
        print('何を出しますか？(グー、チョキ、パー) >>>', end='')
        player = input()

    #cpuの手
    cpu = random.choice(janken)
    print('あなた: ' +player + ' vs ' + cpu + ': cpu')


    if result(player,cpu) == 1:
        print('あなたの勝ちです！')
    elif result(player,cpu) == 2:
        print('あなたの負けです')
    else:
        print('あいこです\nもう1回！')
        game()
game()
