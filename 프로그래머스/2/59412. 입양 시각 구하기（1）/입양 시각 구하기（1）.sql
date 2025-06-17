with recursive time_table as (
    select 9 as `HOUR`
    
    union all
    
    select HOUR + 1
    from time_table
    where HOUR < 19
), temp as (
    select count(*) as `COUNT`, hour(DATETIME) as `HOUR`
    from ANIMAL_OUTS 
    group by hour(DATETIME)
)

select t1.HOUR, t2.COUNT
from time_table t1 
left join temp t2 on t1.HOUR = t2.HOUR
order by HOUR