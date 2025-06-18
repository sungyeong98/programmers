with temp as (
    select 
        ROUTE, 
        round(sum(D_BETWEEN_DIST), 1) as TOTAL_DISTANCE, 
        round(avg(D_BETWEEN_DIST), 2) as AVERAGE_DISTANCE
    from SUBWAY_DISTANCE
    group by ROUTE
    order by TOTAL_DISTANCE desc
)

select
    ROUTE,
    concat(TOTAL_DISTANCE, "km") as TOTAL_DISTANCE,
    concat(AVERAGE_DISTANCE, "km") as AVERAGE_DISTANCE
from temp