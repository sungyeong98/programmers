with fix_len as (
    select
        FISH_TYPE,
        case when LENGTH is null then 10 else LENGTH end as LENGTH
    from FISH_INFO
),
cnt as (
    select
        FISH_TYPE,
        count(*) as cnt
    from FISH_INFO
    group by FISH_TYPE
),
avg_len as (
    select
        FISH_TYPE,
        avg(LENGTH) as len,
        max(LENGTH) as max_len
    from fix_len
    group by FISH_TYPE
    having avg(LENGTH)>=33
)

select
    a.cnt as FISH_COUNT,
    b.max_len as MAX_LENGTH,
    a.FISH_TYPE as FISH_TYPE
from 
    cnt as a,
    avg_len as b
where
    a.FISH_TYPE=b.FISH_TYPE
order by FISH_TYPE