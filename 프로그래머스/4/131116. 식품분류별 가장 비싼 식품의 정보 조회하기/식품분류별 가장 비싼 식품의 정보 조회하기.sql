with temp as (
    select CATEGORY, max(PRICE) as PRICE
    from FOOD_PRODUCT
    group by CATEGORY having CATEGORY in ('과자', '국', '김치', '식용유')
)

select f.CATEGORY, f.PRICE as MAX_PRICE, f.PRODUCT_NAME
from FOOD_PRODUCT f
join temp t on f.CATEGORY = t.CATEGORY and f.PRICE = t.PRICE
order by MAX_PRICE desc