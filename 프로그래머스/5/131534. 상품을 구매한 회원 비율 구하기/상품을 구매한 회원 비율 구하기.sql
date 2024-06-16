with
valid_user as (
    select USER_ID
    from USER_INFO
    where year(JOINED)=2021
),
valid_total_user as (
    select count(*) as total
    from valid_user
),
valid_sale as (
    select distinct
        USER_ID,
        year(SALES_DATE) as YEAR,
        month(SALES_DATE) as MONTH
    from ONLINE_SALE
    where USER_ID in (select USER_ID from valid_user)
),
result as (
    select
        a.YEAR as YEAR,
        a.MONTH as MONTH,
        count(a.MONTH) as PURCHASED_USERS,
        round(count(a.MONTH) / b.total, 1) as PUCHASED_RATIO
    from valid_sale as a, valid_total_user as b
    group by a.YEAR, a.MONTH
)

select * from result
order by YEAR, MONTH