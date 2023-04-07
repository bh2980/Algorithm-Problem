# 2022년 10월에 작성 게시글
# 댓글 작성일 기준 오름차순, 게시글 제목 기준 오름차순
SELECT B.TITLE, B.board_id, R.reply_id, R.writer_id, R.contents, date_format(R.created_date, '%Y-%m-%d')
from USED_GOODS_BOARD as B, USED_GOODS_REPLY as R
where B.board_id = R.board_id
and year(B.CREATED_DATE) = 2022 and month(B.CREATED_DATE) = 10
order by R.CREATED_DATE, B.TITLE