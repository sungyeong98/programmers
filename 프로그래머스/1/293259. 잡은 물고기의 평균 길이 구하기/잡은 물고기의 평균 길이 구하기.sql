select
    round(avg(if(LENGTH > 10, LENGTH, 10)), 2) as AVERAGE_LENGTH
from FISH_INFO