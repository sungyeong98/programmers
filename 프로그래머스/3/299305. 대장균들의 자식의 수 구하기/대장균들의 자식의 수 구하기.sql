with cnt as (
    select
        PARENT_ID,
        count(PARENT_ID) as cnt
    from ECOLI_DATA 
    group by PARENT_ID
    having PARENT_ID is not null
)

select
    a.ID as ID,
    coalesce(b.cnt,0) as CHILD_COUNT
from ECOLI_DATA as a
left join cnt as b
    on a.ID=b.PARENT_ID
order by a.ID