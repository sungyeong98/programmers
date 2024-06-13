select
    extract(month from START_DATE) as MONTH,
    CAR_ID,
    count(CAR_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where
    CAR_ID in (
        select CAR_ID
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where extract(month from START_DATE) between 8 and 10
        group by CAR_ID
        having count(CAR_ID)>=5
    ) and
    extract(month from START_DATE) between 8 and 10
group by MONTH, CAR_ID
having count(CAR_ID)>0
order by MONTH, CAR_ID desc