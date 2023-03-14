-- 코드를 입력하세요 
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE,'%Y-%m-%d')
FROM USED_GOODS_BOARD B, USED_GOODS_REPLY R
WHERE DATE_FORMAT(B.CREATED_DATE,'%Y%m') = 202210
    AND B.BOARD_ID = R.BOARD_ID
ORDER BY R.CREATED_DATE, B.TITLE;