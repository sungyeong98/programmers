select p.PRODUCT_CODE, sum(o.SALES_AMOUNT) * p.PRICE as SALES
from PRODUCT p
join OFFLINE_SALE o on p.PRODUCT_ID = o.PRODUCT_ID
group by o.PRODUCT_ID
order by SALES desc, PRODUCT_CODE