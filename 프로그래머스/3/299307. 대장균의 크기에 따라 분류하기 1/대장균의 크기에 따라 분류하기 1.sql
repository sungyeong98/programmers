select
    ID,
    case
        when SIZE_OF_COLONY<=100 then 'LOW'
        when SIZE_OF_COLONY between 101 and 1000 then 'MEDIUM'
        when SIZE_OF_COLONY>=1001 then 'HIGH'
    end as SIZE
from ECOLI_DATA
order by ID