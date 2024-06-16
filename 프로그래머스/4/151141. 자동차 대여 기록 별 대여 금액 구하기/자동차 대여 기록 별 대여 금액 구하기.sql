with car_type as (
    select distinct CAR_ID,CAR_TYPE,DAILY_FEE
    from CAR_RENTAL_COMPANY_CAR 
    where
        CAR_TYPE = '트럭'
),
his as (
    select
        h.CAR_ID,
        h.HISTORY_ID as HISTORY_ID,
        datediff(h.END_DATE,h.START_DATE)+1 as period,
        c.DAILY_FEE as price,
        h.START_DATE,
        h.END_DATE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    inner join car_type as c 
        on h.CAR_ID=c.CAR_ID
),
dis as (
    select
        CAR_TYPE,
        DURATION_TYPE,
        (100-DISCOUNT_RATE)/100 as discount
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
    where CAR_TYPE = '트럭'
)

select 
    his.HISTORY_ID as HISTORY_ID,
    case
        when his.period<7 then (his.price * his.period)
        when his.period between 7 and 29 then round(his.price * (select discount from dis where DURATION_TYPE like '7%')*his.period)
        when his.period between 30 and 89 then round(his.price * (select discount from dis where DURATION_TYPE like '30%')*his.period)
        when his.period>=90 then round(his.price * (select discount from dis where DURATION_TYPE like '90%')*his.period)
    end as FEE
from his
order by
    FEE desc, HISTORY_ID desc