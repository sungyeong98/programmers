select distinct
    CART_ID
from CART_PRODUCTS
where
    CART_ID in (
        select
            CART_ID
        from CART_PRODUCTS 
        where
            NAME like '%Milk%'
    ) and
    CART_ID in (
        select
            CART_ID
        from CART_PRODUCTS 
        where
            NAME like '%Yogurt%'
    )
order by CART_ID