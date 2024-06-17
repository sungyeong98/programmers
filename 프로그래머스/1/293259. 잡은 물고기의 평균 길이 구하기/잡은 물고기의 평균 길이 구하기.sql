select
    round(avg(LENGTH),2) as AVERAGE_LENGTH
from (
    select case
        when LENGTH is null then 10 else LENGTH
        end as LENGTH
    from FISH_INFO
) temp