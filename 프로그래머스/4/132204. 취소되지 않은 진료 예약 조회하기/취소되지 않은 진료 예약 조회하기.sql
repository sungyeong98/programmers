-- 코드를 입력하세요
SELECT
    a.APNT_NO as APNT_NO,
    p.PT_NAME as PT_NAME,
    a.PT_NO as PT_NO,
    a.MCDP_CD as MCDP_CD,
    d.DR_NAME as DR_NAME,
    a.APNT_YMD as APNT_YMD
from 
    APPOINTMENT as a,
    DOCTOR as d,
    PATIENT as p
where
    a.PT_NO=p.PT_NO and
    d.DR_ID=a.MDDR_ID and
    date_format(a.APNT_YMD,'%Y-%m-%d')='2022-04-13' and a.APNT_CNCL_YN='N'
order by APNT_YMD