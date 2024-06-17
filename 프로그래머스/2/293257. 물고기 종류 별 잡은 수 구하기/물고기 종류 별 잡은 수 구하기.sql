select
    count(*) as FISH_COUNT,
    b.FISH_NAME as FISH_NAME
from FISH_INFO as a, FISH_NAME_INFO as b
where a.FISH_TYPE=b.FISH_TYPE
group by b.FISH_NAME
order by FISH_COUNT desc