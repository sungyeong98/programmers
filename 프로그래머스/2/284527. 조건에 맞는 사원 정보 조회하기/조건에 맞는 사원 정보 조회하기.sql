with high as (
    select
        EMP_NO,
        sum(SCORE) as sum_score
    from HR_GRADE
    group by EMP_NO
    order by sum(SCORE) desc
    limit 1
)

select
    b.sum_score as SCORE,
    a.EMP_NO as EMP_NO,
    a.EMP_NAME as EMP_NAME,
    a.POSITION as POSITION,
    a.EMAIL as EMAIL
from
    HR_EMPLOYEES as a,
    high as b
where
    a.EMP_NO=b.EMP_NO