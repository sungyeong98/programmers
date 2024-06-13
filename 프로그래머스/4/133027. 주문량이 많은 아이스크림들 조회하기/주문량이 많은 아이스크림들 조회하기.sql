select
    a.FLAVOR as FLAVOR
from
    FIRST_HALF as a,
    JULY as b
where
    a.FLAVOR=b.FLAVOR
group by a.FLAVOR
order by sum(a.TOTAL_ORDER)+sum(b.TOTAL_ORDER) desc
limit 3