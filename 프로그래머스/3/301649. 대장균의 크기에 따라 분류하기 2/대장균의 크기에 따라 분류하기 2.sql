with temp as (
    select
        ID,
        ntile(4) over (order by SIZE_OF_COLONY) as q
    from ECOLI_DATA 
)
select
    ID,
    case
        when q=4 then 'CRITICAL'
        when q=3 then 'HIGH'
        when q=2 then 'MEDIUM'
        when q=1 then 'LOW'
    end as COLONY_NAME
from temp
order by ID