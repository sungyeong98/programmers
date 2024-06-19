select
    child.ID as ID,
    child.GENOTYPE as GENOTYPE,
    parent.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA as child
left join ECOLI_DATA as parent
    on child.PARENT_ID=parent.ID
where child.GENOTYPE & parent.GENOTYPE = parent.GENOTYPE
order by ID