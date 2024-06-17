with avg_sal as (
    select
        DEPT_ID,
        round(avg(SAL)) as AVG_SAL
    from HR_EMPLOYEES 
    group by DEPT_ID
)

select 
    a.DEPT_ID as DEPT_ID,
    a.DEPT_NAME_EN as DEPT_NAME_EN,
    b.AVG_SAL as AVG_SAL
from HR_DEPARTMENT as a, avg_sal as b
where a.DEPT_ID=b.DEPT_ID
order by AVG_SAL desc