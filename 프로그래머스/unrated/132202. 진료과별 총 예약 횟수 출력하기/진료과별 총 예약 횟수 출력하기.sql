-- 코드를 입력하세요
SELECT MCDP_CD, COUNT(APNT_YMD) AS 5월예약건수
FROM APPOINTMENT
WHERE MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_cD ASC