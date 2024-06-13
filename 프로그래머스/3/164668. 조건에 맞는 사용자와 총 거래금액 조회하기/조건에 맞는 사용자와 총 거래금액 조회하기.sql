select
    a.WRITER_ID as WRITER_ID,
    b.NICKNAME as NICKNAME,
    sum(a.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as a
inner join USED_GOODS_USER as b
    on a.WRITER_ID=b.USER_ID
where
    a.STATUS='DONE'
group by a.WRITER_ID
having sum(a.PRICE)>=700000
order by TOTAL_SALES