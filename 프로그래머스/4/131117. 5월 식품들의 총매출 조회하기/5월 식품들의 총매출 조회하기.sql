with temp as (
    select PRODUCT_ID, sum(AMOUNT) as AMOUNT
    from FOOD_ORDER
    where year(PRODUCE_DATE) = 2022 and month(PRODUCE_DATE) = 5
    group by PRODUCT_ID
)

select p.PRODUCT_ID, p.PRODUCT_NAME, p.PRICE * t.AMOUNT as TOTAL_SALES
from FOOD_PRODUCT p
join temp t on p.PRODUCT_ID = t.PRODUCT_ID
order by TOTAL_SALES desc, PRODUCT_ID