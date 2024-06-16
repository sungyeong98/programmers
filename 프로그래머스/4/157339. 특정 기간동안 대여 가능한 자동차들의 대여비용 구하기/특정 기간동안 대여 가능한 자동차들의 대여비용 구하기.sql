with car_type as (
    select CAR_ID,CAR_TYPE,DAILY_FEE
    from CAR_RENTAL_COMPANY_CAR 
    where CAR_TYPE in ('세단','SUV')
), pos as (
    select distinct
        CAR_ID,CAR_TYPE,DAILY_FEE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    join car_type using(CAR_ID)
    where
        CAR_ID not in (
            select CAR_ID
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where
                (END_DATE between '2022-11-01 00:00:00' and '2022-11-30 00:00:00') or
                (START_DATE between '2022-11-01 00:00:00' and '2022-11-30 00:00:00') or
                (START_DATE < '2022-11-01 00:00:00' and END_DATE > '2022-11-30 00:00:00')
        )
), dis as (
    select 
        CAR_TYPE,
        (100-DISCOUNT_RATE)*0.01 as price
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
    where
        CAR_TYPE in ('세단','SUV') and
        DURATION_TYPE like '30%'
)

select
    pos.CAR_ID as CAR_ID,
    CAR_TYPE,
    round(pos.DAILY_FEE*dis.price*30) as FEE
from pos
join dis using(CAR_TYPE)
where
    round(pos.DAILY_FEE*dis.price*30)>=500000 and
    round(pos.DAILY_FEE*dis.price*30)<2000000
order by 
    FEE desc, CAR_TYPE, CAR_ID desc