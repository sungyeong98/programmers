with temp1 as (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by count(*) desc
    limit 1
), temp2 as (
    select t1.MEMBER_ID, m.MEMBER_NAME
    from temp1 t1
    join MEMBER_PROFILE m on t1.MEMBER_ID = m.MEMBER_ID
)

select t2.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
from temp2 t2
join REST_REVIEW r on t2.MEMBER_ID = r.MEMBER_ID
order by REVIEW_DATE