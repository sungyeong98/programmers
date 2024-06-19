with max_size as (
    select
        year(DIFFERENTIATION_DATE) as YEAR,
        max(SIZE_OF_COLONY) as size
    from ECOLI_DATA 
    group by year(DIFFERENTIATION_DATE)
)

select
    year(a.DIFFERENTIATION_DATE) as YEAR,
    (b.size - a.SIZE_OF_COLONY) as YEAR_DEV,
    a.ID as ID
from
    ECOLI_DATA as a,
    max_size as b
where
    year(a.DIFFERENTIATION_DATE)=b.YEAR
order by
    YEAR, YEAR_DEV