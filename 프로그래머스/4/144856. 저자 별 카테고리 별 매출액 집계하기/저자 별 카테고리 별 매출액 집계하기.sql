select
    a.AUTHOR_ID as AUTHOR_ID,
    b.AUTHOR_NAME as AUTHOR_NAME,
    a.CATEGORY as CATEGORY,
    sum(temp.sale*a.PRICE) as TOTAL_SALES
from
    (
        select
            extract(month from SALES_DATE) as month,
            BOOK_ID,
            sum(SALES) as sale
        from BOOK_SALES
        where extract(month from SALES_DATE)=1
        group by extract(month from SALES_DATE),BOOK_ID
    ) as temp,
    BOOK as a,
    AUTHOR as b
where
    a.AUTHOR_ID=b.AUTHOR_ID and
    a.BOOK_ID=temp.BOOK_ID
group by
    b.AUTHOR_NAME, a.CATEGORY
order by 
    AUTHOR_ID,CATEGORY desc