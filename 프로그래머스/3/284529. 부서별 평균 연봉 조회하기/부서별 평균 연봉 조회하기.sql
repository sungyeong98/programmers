with temp as (
    select DEPT_ID, round(avg(SAL)) as AVG_SAL
    from HR_EMPLOYEES
    group by DEPT_ID
)

select t.DEPT_ID, d.DEPT_NAME_EN, t.AVG_SAL
from temp t
join HR_DEPARTMENT d on t.DEPT_ID = d.DEPT_ID
order by AVG_SAL desc