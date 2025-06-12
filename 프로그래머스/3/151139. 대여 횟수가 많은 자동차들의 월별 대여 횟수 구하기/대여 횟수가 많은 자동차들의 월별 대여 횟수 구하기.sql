with temp as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where year(START_DATE) = 2022 and month(START_DATE) between 8 and 10
    group by CAR_ID having count(CAR_ID) >= 5
)

select
    month(c.START_DATE) as MONTH,
    c.CAR_ID,
    count(c.CAR_ID) as RECORDS
from temp t
join CAR_RENTAL_COMPANY_RENTAL_HISTORY c on t.CAR_ID = c.CAR_ID
where year(c.START_DATE) = 2022 and month(c.START_DATE) between 8 and 10
group by MONTH, CAR_ID
order by MONTH, CAR_ID desc