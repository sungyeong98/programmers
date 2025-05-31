with temp as (
    select ITEM_ID
    from ITEM_TREE
    where PARENT_ITEM_ID is null
)

select t.ITEM_ID, i.ITEM_NAME
from temp t
join ITEM_INFO i on t.ITEM_ID = i.ITEM_ID
order by ITEM_ID