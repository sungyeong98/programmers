with temp as (
    select WRITER_ID, sum(PRICE) as TOTAL_SALES
    from USED_GOODS_BOARD
    where STATUS = "DONE"
    group by WRITER_ID
)

select u.USER_ID, u.NICKNAME, t.TOTAL_SALES
from temp t
join USED_GOODS_USER u on t.WRITER_ID = u.USER_ID
where TOTAL_SALES >= 700000
order by TOTAL_SALES