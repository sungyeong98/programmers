select
    a.CATEGORY,
    sum(b.total_sales) as TOTAL_SALES
from (
    select
        BOOK_ID,
        sum(SALES) as total_sales
    from BOOK_SALES
    where date_format(SALES_DATE,'%Y-%m')='2022-01'
    group by BOOK_ID
) as b
inner join BOOK as a
    on a.BOOK_ID=b.BOOK_ID
group by a.CATEGORY
order by a.CATEGORY