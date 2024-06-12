-- 코드를 입력하세요
SELECT
    i.REST_ID as REST_ID,
    i.REST_NAME as REST_NAME,
    i.FOOD_TYPE as FOOD_TYPE,
    i.FAVORITES as FAVORITES,
    i.ADDRESS as ADDRESS,
    r.score as SCORE
from
    REST_INFO as i,
    (
        select
            REST_ID, round(avg(REVIEW_SCORE),2) as score
        from REST_REVIEW
        group by REST_ID
    ) as r
where
    i.REST_ID=r.REST_ID and
    ADDRESS like '서울%'
order by 
    SCORE desc, FAVORITES desc