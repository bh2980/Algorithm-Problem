# 2021년에 가입
# 나이가 20세 이상 29세 이하
# 인 회원 수 count
select count(*)
from user_info
where year(JOINED) = 2021
and 20 <= age and age <= 29