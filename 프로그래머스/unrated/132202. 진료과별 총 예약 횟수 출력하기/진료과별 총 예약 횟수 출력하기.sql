# 2022년 5월 예약
# 진료과코드별 예약 환자수
# 환자수 기준 오름차순, 진료과 코드 내림차순
SELECT MCDP_CD as '진료과코드', count(MCDP_CD) as '5월예약건수'
FROM APPOINTMENT 
WHERE YEAR(APNT_YMD) = 2022 and MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY count(MCDP_CD), MCDP_CD