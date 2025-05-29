with temp as (
    select distinct
        extract(year from s.SALES_DATE) as YEAR,
        extract(month from s.SALES_DATE) as MONTH,
        i.GENDER,
        i.USER_ID
    from USER_INFO i
    join ONLINE_SALE s on i.USER_ID = s.USER_ID
    where i.GENDER is not NULL
)
select YEAR, MONTH, GENDER, count(USER_ID) as USERS
from temp
group by YEAR, MONTH, GENDER
order by YEAR, MONTH, GENDER