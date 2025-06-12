with temp1 as (
    select FLAVOR, sum(TOTAL_ORDER) as PRICE
    from FIRST_HALF
    group by FLAVOR
), temp2 as (
    select FLAVOR, sum(TOTAL_ORDER) as PRICE
    from JULY
    group by FLAVOR
)

select t1.FLAVOR
from temp1 t1 join temp2 t2 on t1.FLAVOR = t2.FLAVOR
order by t1.PRICE + t2.PRICE desc
limit 3