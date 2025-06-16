with temp as (
    select BOOK_ID, SALES
    from BOOK_SALES
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
)

select b.CATEGORY, sum(t.SALES) as TOTAL_SALES
from BOOK b
join temp t on b.BOOK_ID = t.BOOK_ID
group by b.CATEGORY
order by CATEGORY