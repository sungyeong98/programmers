with pos_item as (
    select
        ITEM_ID
    from ITEM_INFO
    where RARITY='RARE'
),
next_item as (
    select
        ITEM_ID
    from ITEM_TREE
    where
        PARENT_ITEM_ID is not null and
        PARENT_ITEM_ID in (select * from pos_item)
)
select
    a.ITEM_ID as ITEM_ID,
    a.ITEM_NAME as ITEM_NAME,
    a.RARITY as RARITY
from 
    ITEM_INFO as a,
    next_item as b
where a.ITEM_ID=b.ITEM_ID
order by
    ITEM_ID desc