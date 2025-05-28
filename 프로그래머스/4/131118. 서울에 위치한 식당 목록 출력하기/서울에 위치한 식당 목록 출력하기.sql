select
    i.REST_ID as REST_ID,
    i.REST_NAME as REST_NAME,
    i.FOOD_TYPE as FOOD_TYPE,
    i.FAVORITES as FAVORITES,
    i.ADDRESS as ADDRESS,
    r.SCORE as SCORE
from REST_INFO i 
join (
    select REST_ID, round(avg(REVIEW_SCORE), 2) as SCORE
    from REST_REVIEW
    group by REST_ID
) r on i.REST_ID = r.REST_ID
where i.ADDRESS like "서울%"
order by SCORE desc, FAVORITES desc