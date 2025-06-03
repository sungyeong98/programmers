select count(*) as COUNT
from ECOLI_DATA
where GENOTYPE & 2 = 0 and (GENOTYPE & 1 = 1 or GENOTYPE & 4 = 4)
-- 2번 형질은 없어야 함 -> 2번 비트는 0이어야 함
-- 1번 형질 혹은 3번 형질은 존재해야함 -> 1번 비트, 4번 비트는 1 or 4이어야 함