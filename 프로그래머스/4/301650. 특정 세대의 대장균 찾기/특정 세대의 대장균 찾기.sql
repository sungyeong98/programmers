with first_gen as (
    select ID
    from ECOLI_DATA 
    where PARENT_ID is null
), second_gen as (
    select ID
    from ECOLI_DATA
    where PARENT_ID in (select * from first_gen)
), third_gen as (
    select ID
    from ECOLI_DATA
    where PARENT_ID in (select * from second_gen)
)
select * from third_gen
order by ID