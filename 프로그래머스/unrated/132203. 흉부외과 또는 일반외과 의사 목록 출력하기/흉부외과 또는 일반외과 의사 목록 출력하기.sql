# CS거나 GS인 의사의 이름
# 고용일자 내림차순, 같아면 이름 오름차순
SELECT DR_NAME, DR_ID, MCDP_CD, date_format(HIRE_YMD, '%Y-%m-%d')
FROM DOCTOR
WHERE MCDP_CD = 'CS' or MCDP_CD = 'GS'
order by hire_ymd desc, dr_name