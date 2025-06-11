with temp as (
    select max(SIZE_OF_COLONY) as MAX_SIZE, year(DIFFERENTIATION_DATE) as YEAR
    from ECOLI_DATA
    group by year(DIFFERENTIATION_DATE)
)

select 
    t.YEAR, 
    (t.MAX_SIZE - d.SIZE_OF_COLONY) as YEAR_DEV,
    d.ID
from ECOLI_DATA d
join temp t on t.YEAR = year(d.DIFFERENTIATION_DATE)
order by YEAR, YEAR_DEV