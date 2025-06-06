with gen2 as (
    select c.ID
    from ECOLI_DATA p
    join ECOLI_DATA c on p.ID = c.PARENT_ID
    where p.PARENT_ID is null
), gen3 as (
    select c.ID
    from gen2 p
    join ECOLI_DATA c on p.ID = c.PARENT_ID
)

select * from gen3 order by ID