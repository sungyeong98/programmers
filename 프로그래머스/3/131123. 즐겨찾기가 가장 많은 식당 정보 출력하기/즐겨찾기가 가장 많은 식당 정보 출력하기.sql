with temp as (
    select
        FOOD_TYPE,
        max(FAVORITES) as FAVORITES
    from REST_INFO
    group by FOOD_TYPE
)

select
    i.FOOD_TYPE as FOOD_TYPE,
    i.REST_ID as REST_ID,
    i.REST_NAME as REST_NAME,
    i.FAVORITES as FAVORITES
from REST_INFO as i
inner join temp as t
    on i.FOOD_TYPE=t.FOOD_TYPE and i.FAVORITES=t.FAVORITES
order by FOOD_TYPE desc
