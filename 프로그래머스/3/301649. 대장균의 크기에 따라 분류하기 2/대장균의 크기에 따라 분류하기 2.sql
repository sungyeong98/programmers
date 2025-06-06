with temp as (
    select 
        ID,
        ntile(4) over(order by SIZE_OF_COLONY) as SIZE
    from ECOLI_DATA
)

select ID,
    case
        when SIZE = 1 then "LOW"
        when SIZE = 2 then "MEDIUM"
        when SIZE = 3 then "HIGH"
        else "CRITICAL"
    end as COLONY_NAME
from temp
order by ID