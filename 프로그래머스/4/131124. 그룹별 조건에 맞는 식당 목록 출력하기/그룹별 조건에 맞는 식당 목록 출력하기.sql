with max_review as (
    select
        MEMBER_ID
    from
        REST_REVIEW
    group by MEMBER_ID
    order by count(MEMBER_ID) desc
    limit 1
)

select
    p.MEMBER_NAME as MEMBER_NAME,
    r.REVIEW_TEXT as REVIEW_TEXT,
    date_format(r.REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW as r
inner join MEMBER_PROFILE as p
    on r.MEMBER_ID=p.MEMBER_ID
where
    r.MEMBER_ID in (
        select MEMBER_ID
        from max_review
    )
order by
    REVIEW_DATE,REVIEW_TEXT