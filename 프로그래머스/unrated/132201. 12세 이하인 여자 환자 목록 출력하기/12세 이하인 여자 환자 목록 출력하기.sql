# 12세 이하인
# 여자 환자
# 전화번호가 없다면 NONE으로 출력
# 나이 기준 내림차순, 나이가 같다면 환자 이름 오름차순

SELECT pt_name, pt_no, gend_cd, age, ifnull(tlno, "NONE")
from PATIENT 
where age <= 12
and gend_cd = 'W'
order by age desc, pt_name