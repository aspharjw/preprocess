# REQUIRE PACKAGE : xlrd , konlpy
import initialize
import postag

# postag 파일의 PosTag 클래스는 여러가지 트랜스폼 모듈을 갖고 있다
postagger = postag.PosTag()

# initialize 파일의 xl_to_BookingReview 모듈은
# 엑셀파일 입력을 받고 BookingReview list 을 리턴한다

# BookingReview 클래스 변수들과 형식은 다음과 같다
#   company : str
#   id : str
#   rate : str
#   context : str
#   post_time : str
#   spam_ham : str
#   context_backup : str
items = initialize.xl_to_BookingReview('snuproject_bookingreviews.xlsx')

# PosTag 클래스의 트랜스폼 모듈을 실행하면 BookingReview 변수 형식이 바뀐다
# hannanum 모듈 같은 경우는 다음과 같다
#
# BookingReview :
#   company : str
#   id : str
#   rate : str
#   context : tuple list
#   post_time : str
#   spam_ham : str
#   context_backup : str
postagger.hannanum(items)

# BookingReview list 를 모두 출력해본다
for item in items:
    print(item)
