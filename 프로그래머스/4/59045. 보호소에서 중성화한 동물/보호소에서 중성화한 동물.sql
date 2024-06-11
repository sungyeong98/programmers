select
    ANIMAL_ID,
    ANIMAL_TYPE,
    NAME
from ANIMAL_OUTS
where
    ANIMAL_ID in (
        select
            ANIMAL_ID
        from ANIMAL_INS
        where SEX_UPON_INTAKE like '%Intact%'
    ) and
    (SEX_UPON_OUTCOME like '%Spayed%' or SEX_UPON_OUTCOME like '%Neutered%')
order by ANIMAL_ID