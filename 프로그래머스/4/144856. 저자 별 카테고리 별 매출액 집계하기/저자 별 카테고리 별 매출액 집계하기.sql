with temp1 as (
    select BOOK_ID, SALES
    from BOOK_SALES
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
), temp2 as (
    select 
        b.CATEGORY, 
        b.AUTHOR_ID, 
        sum(b.PRICE * t.SALES) as TOTAL_PRICE
    from BOOK b
    join temp1 t on b.BOOK_ID = t.BOOK_ID
    group by AUTHOR_ID, CATEGORY
)

select 
    a.AUTHOR_ID, a.AUTHOR_NAME, t.CATEGORY,
    t.TOTAL_PRICE
from AUTHOR a
join temp2 t on a.AUTHOR_ID = t.AUTHOR_ID
order by AUTHOR_ID, CATEGORY desc