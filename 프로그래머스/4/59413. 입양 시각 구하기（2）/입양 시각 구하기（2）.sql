with recursive hour_list as (
    select 0 as hour
    union all
    
    select hour+1
    from hour_list
    where hour<23
)

select
    a.hour as HOUR,
    count(b.ANIMAL_ID) as COUNT
from hour_list as a
left join ANIMAL_OUTS as b
    on a.hour=extract(hour from b.DATETIME)
group by a.hour
order by HOUR