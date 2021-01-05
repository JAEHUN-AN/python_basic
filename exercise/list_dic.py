p1 = {'id' : 1 ,'name' : 'hong kildong', 'email' : 'hong@mail.com', 'hp_num' : '010-2343-9870'}
p2 = {'id' : 2 ,'name' : 'lee soonsin', 'email' : 'lee@mail.com', 'hp_num' : '010-3333-5555'}
p3 = {'id' : 3 ,'name' : 'jang youngsil', 'email' : 'jang@mail.com', 'hp_num' : '010-7777-1234'}
p4 = {'id' : 4 ,'name' : 'king sejon', 'email' : 'king@mail.com', 'hp_num' : '010-4567-0987'}

p = list()
p = [p1,p2,p3,p4]

for i in p :
    for k, v in i.items():
        print(k, v)