select
    a.year as YEAR,
    a.month as MONTh,
    a.GENDER as GENDER,
    count(a.USER_ID) as USERS
from 
    (
        select distinct
            extract(year from o.SALES_DATE) as year,
            extract(month from o.SALES_DATE) as month,
            i.GENDER as GENDER,
            i.USER_ID as USER_ID
        from
            USER_INFO as i
        inner join ONLINE_SALE as o
            on i.USER_ID=o.USER_ID
        where
            GENDER is not null
    ) as a
group by
    YEAR,MONTH,GENDER
order by
    YEAR,MONTH,GENDER