with convert_bin as (
    select ID, EMAIL, FIRST_NAME, LAST_NAME, conv(SKILL_CODE,10,2) as num
    from DEVELOPERS
), reverse_bin as (
    select ID, EMAIL, FIRST_NAME, LAST_NAME, reverse(num) as rev_num
    from convert_bin
), find_pos as (
    select log2(CODE) +1 as position
    from SKILLCODES 
    where CATEGORY='Front End'
), temp as (
    select ID, EMAIL, FIRST_NAME, LAST_NAME
    from reverse_bin as a
    join find_pos as b
        on substring(a.rev_num, b.position, 1)='1'
)
select * from temp
group by ID, EMAIL, FIRST_NAME, LAST_NAME
order by ID