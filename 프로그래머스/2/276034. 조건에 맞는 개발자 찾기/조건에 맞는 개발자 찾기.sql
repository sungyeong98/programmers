with convert_bin as (
    select ID, EMAIL, FIRST_NAME, LAST_NAME, conv(SKILL_CODE,10,2) as num
    from DEVELOPERS 
), reverse_bin as (
    select ID, EMAIL, FIRST_NAME, LAST_NAME, reverse(num) as rev_num
    from convert_bin
), pos_1 as (
    select
        log2(CODE)+1 as position
    from SKILLCODES
    where NAME='C#'
), pos_2 as (
    select
        log2(CODE)+1 as position
    from SKILLCODES
    where NAME='Python'
), result as (
    select ID, EMAIL, FIRST_NAME, LAST_NAME
    from reverse_bin
    where 
        substring(rev_num,(select position from pos_1),1)='1' or
        substring(rev_num,(select position from pos_2),1)='1'
)
select * from result
order by ID