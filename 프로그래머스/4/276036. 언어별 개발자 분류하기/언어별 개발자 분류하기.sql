with grade_a as (
    select distinct ID
    from DEVELOPERS as a
    join (
        select CODE from SKILLCODES
        where CATEGORY='Front End'
    ) as b
        on a.SKILL_CODE & b.CODE > 0
    join (
        select CODE from SKILLCODES 
        where NAME='Python'
    ) as c
        on a.SKILL_CODE & c.CODE > 0
), grade_b as (
    select distinct ID
    from DEVELOPERS as a
    join (
        select CODE from SKILLCODES
        where NAME='C#'
    ) as b
        on a.SKILL_CODE & b.CODE > 0
), grade_c as (
    select distinct ID
    from DEVELOPERS as a
    join (
        select CODE from SKILLCODES
        where CATEGORY='Front End'
    ) as b
        on a.SKILL_CODE & b.CODE > 0
)

select
    case
        when ID in (select ID from grade_a) then 'A'
        when ID in (select ID from grade_b) then 'B'
        when ID in (select ID from grade_c) then 'C'
    end as GRADE,
    ID, EMAIL
from DEVELOPERS
where
    ID in (
        select ID from grade_a
        union
        select ID from grade_b
        union
        select ID from grade_c
    )
order by GRADE, ID