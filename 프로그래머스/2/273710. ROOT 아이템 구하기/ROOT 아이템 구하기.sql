select
    a.ITEM_ID as ITEM_ID,
    a.ITEM_NAME as ITEM_NAME
from ITEM_INFO as a, ITEM_TREE as b
where
    a.ITEM_ID=b.ITEM_ID and
    b.PARENT_ITEM_ID is null
order by ITEM_ID