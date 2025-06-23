select
    ANIMAL_TYPE,
    case
        when NAME is not null then NAME else "No name"
    end as NAME,
    SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID