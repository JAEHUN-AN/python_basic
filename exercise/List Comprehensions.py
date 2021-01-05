books = list()
# 책 목록 선언
# 책 목록 만들기
books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28', '출판사':'A출판', '쪽수':200, '추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', '출판사':'B 출판', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', '출판사':'A출판', '쪽수':296, '추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', '출판사':'B출판', '쪽수':526, '추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', '출판사':'C출판', '쪽수':248, '추천유무':True})
print(books)
#1.250쪽 넘는 책 목록 만들기
book_250 = list()
for i in books :
    if i['쪽수'] > 250:
        book_250.append(i['제목'])
#print(book_250)

#2.추천유무가 True인 책 목록 만들기
book_rec = list()
for i in books :
    if i['추천유무'] == True:
        book_rec.append(i['제목'])
print(book_rec)

#3.출판사 목록 만들기 ( 중복되는 이름은 제거합니다.)
book_pub = list()
for i in books :
    if i['출판사'] not in book_pub:
        book_pub.append(i['출판사'])
print(book_pub)
