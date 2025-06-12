with temp as (
    select *
    from ANIMAL_INS
    where SEX_UPON_INTAKE like "Intact%"
)

select t.ANIMAL_ID, t.ANIMAL_TYPE, t.NAME
from temp t
join ANIMAL_OUTS o on t.ANIMAL_ID = o.ANIMAL_ID
where SEX_UPON_OUTCOME like "Spayed%" or SEX_UPON_OUTCOME like "Neutered%"
order by ANIMAL_ID