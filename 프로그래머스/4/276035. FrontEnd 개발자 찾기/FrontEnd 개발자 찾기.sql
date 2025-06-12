with temp as (
    select sum(CODE) as CODE
    from SKILLCODES
    where CATEGORY = "Front End"
)

select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS d, temp t
where d.SKILL_CODE & t.CODE > 0
order by ID