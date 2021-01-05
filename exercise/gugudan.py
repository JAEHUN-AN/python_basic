while True:
    print('구구단 몇 단을 계산할까요(1~9)?')
    k = int(input())

    if k > 9 or k < 1:
        print(0)
        break

    print('구구단 {}단을 계산합니다.'.format(k))
    for i in range(1, 10):
        print("{} * {} = {}".format(k, i, k * i))

print('구구단 게임을 종료합니다.')
