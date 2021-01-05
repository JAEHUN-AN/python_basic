import random

guess_number = random.randint(1, 100)
n = int(input())
cnt = 1

while n != guess_number:
    if n > guess_number:
        print('숫자가 너무 큽니다')
    elif n < guess_number :
        print('숫자가 너무 작습니다')
    n = int(input())
    cnt += 1

print('정답 {}, {}번'.format(guess_number, cnt))