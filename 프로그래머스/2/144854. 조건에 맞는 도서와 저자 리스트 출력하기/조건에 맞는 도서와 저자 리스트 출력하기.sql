with temp as (
    select BOOK_ID, PUBLISHED_DATE, AUTHOR_ID
    from BOOK
    where CATEGORY = "경제"
)
select t.BOOK_ID, a.AUTHOR_NAME, date_format(t.PUBLISHED_DATE, "%Y-%m-%d") as PUBLISHED_DATE
from AUTHOR a
join temp t on a.AUTHOR_ID = t.AUTHOR_ID
order by PUBLISHED_DATE