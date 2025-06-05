with temp as (
    select PARENT_ID, count(*) as CHILD_COUNT
    from ECOLI_DATA
    group by PARENT_ID
    having PARENT_ID is not null
)

select 
    d.ID,
    case when t.CHILD_COUNT is null then 0 else CHILD_COUNT end as CHILD_COUNT
from ECOLI_DATA d
left join temp t on d.ID = t.PARENT_ID
order by ID