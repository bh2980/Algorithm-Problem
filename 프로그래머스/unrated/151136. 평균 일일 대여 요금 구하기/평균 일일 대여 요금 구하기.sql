# SUV인 차들의 평균 일일 대여 요금
SELECT round(avg(DAILY_FEE))
from CAR_RENTAL_COMPANY_CAR 
where CAR_TYPE = 'SUV'