with cnt as (
    select *
    from ECOLI_DATA 
    where
        GENOTYPE & 2 = 0 and
        (GENOTYPE & 1 = 1 or GENOTYPE & 4 = 4)
)
select count(*) as COUNT from cnt