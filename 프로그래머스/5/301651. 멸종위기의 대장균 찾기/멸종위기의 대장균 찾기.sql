with recursive temp as (
    select *, 1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is null
    union all
    
    select a.*, b.GENERATION + 1 as GENERATION
    from ECOLI_DATA as a
    inner join temp as b
        on a.PARENT_ID = b.ID  
)
select
    count(a.GENERATION) as COUNT,
    a.GENERATION
from temp as a
left join ECOLI_DATA as b
    on a.ID = b.PARENT_ID
where b.PARENT_ID is null
group by a.GENERATION