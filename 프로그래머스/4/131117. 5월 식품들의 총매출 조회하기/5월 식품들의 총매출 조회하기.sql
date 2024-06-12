-- 코드를 입력하세요
SELECT
    a.PRODUCT_ID as PRODUCT_ID,
    a.PRODUCT_NAME,
    a.PRICE*b.total_amount as TOTAL_SALES
from FOOD_PRODUCT as a
inner join (
    select PRODUCT_ID,sum(AMOUNT) as total_amount,PRODUCE_DATE
    from FOOD_ORDER
    where
        date_format(PRODUCE_DATE,'%Y-%m')='2022-05'
    group by PRODUCT_ID
) as b
    on a.PRODUCT_ID=b.PRODUCT_ID
order by
    TOTAL_SALES desc, PRODUCT_ID