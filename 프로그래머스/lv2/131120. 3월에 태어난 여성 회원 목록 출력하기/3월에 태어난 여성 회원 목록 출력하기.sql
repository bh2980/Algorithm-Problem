SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(date_of_birth, '%Y-%m-%d') as DATE_OF_BIRTH
from member_profile
where tlno is not null and month(date_of_birth) = 3 and gender = 'W'
order by member_id