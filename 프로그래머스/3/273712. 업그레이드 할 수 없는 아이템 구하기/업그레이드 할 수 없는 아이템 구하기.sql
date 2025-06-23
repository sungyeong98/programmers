with temp as (
    select PARENT_ITEM_ID
    from ITEM_TREE
    where PARENT_ITEM_ID is not null
)

select ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO
where ITEM_ID not in (select * from temp)
order by ITEM_ID desc