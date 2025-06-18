with temp1 as (
    select EMP_NO, sum(SCORE) as SCORE
    from HR_GRADE 
    group by EMP_NO
), temp2 as (
    select t.SCORE, t.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
    from temp1 t
    join HR_EMPLOYEES e on t.EMP_NO = e.EMP_NO
    order by SCORE desc
    limit 1
)

select * from temp2