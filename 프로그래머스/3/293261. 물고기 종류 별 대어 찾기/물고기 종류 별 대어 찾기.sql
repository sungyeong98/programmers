select
    ID, FISH_NAME, LENGTH
from FISH_INFO
join FISH_NAME_INFO using(FISH_TYPE)
where (FISH_TYPE,LENGTH) in (
    select FISH_TYPE, max(LENGTH)
    from FISH_INFO
    group by FISH_TYPE
)
order by ID