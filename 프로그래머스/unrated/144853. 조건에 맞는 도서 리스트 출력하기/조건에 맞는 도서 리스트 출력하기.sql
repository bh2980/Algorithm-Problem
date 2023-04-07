# 2021년 출판
# 인문 카테고리
SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d')
from BOOK
where year(PUBLISHED_DATE) = 2021
and category = '인문'