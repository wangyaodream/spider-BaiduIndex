import os
import random

import pymysql
from qdata.baidu_index import get_search_index


cookie = '''BIDUPSID=9BA35F6F6B7C68489C01A117277A2CA6; PSTM=1700187572; BAIDUID=9BA35F6F6B7C6848951AB48F950F7FA0:FG=1; BDUSS=5Lb1owUVdYZVlicHgyYUhjNXF-anU5RXpNTkZkbGJSV0FPfnZpYmN0UUhMNDVsRVFBQUFBJCQAAAAAAAAAAAEAAAD2HZUDd2FuZ3lhb2RyZWFtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeiZmUHomZlMn; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39712_39780_39678_39817_39834_39839_39904_39909_39934_39937_39932_39942_39940_39938_39931_39783; BAIDUID_BFESS=9BA35F6F6B7C6848951AB48F950F7FA0:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=1; BA_HECTOR=al848485a42h810k2l2l80a21ini2hp1r; ZFY=en4VBi5YlwTUfX6ewbOzBzv1e:B:BApbv:BiD6fqd5XXJo:C; PSINO=7; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1700894043,1701610364,1702436188; bdindexid=o569b0knqeuipaf8h7otq3hlj1; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04524486366POpJIZVUQ3c%2BGenSkIKbPmDtTdqrpQGO3uXb6OgYPy9V5L6wed0iyAhmcvg1Yc6DnMtF3ImE7RYpjdIcJE%2FTtWIMsE9EIRj3%2BDM4Vozia%2BZddWJBCizsnAJw6RQcgnEQkhbkj7u3lh25jrm5Ad0Lh60PXiyHmGn0ujgbttP5NFsEgv5DDDshTYMeGhIjhWVTD%2FSdyC5LhWfL69udwrIWbAOgDsN3NhctsOPh0FT2igHZFEfNEcn3MWSXKRrF648sUIIZk3JJTJk%2Byfi9XHvnU7dEw0ehBHzUR2ijDi91bno%3D38574811173827693750170797605391; __cas__rn__=452448636; __cas__st__212=635e35d76dd46d04254b492f8f92f7029cf2faca0aa914c8d1c179486857bf012253a242a8ee38354a27a513; __cas__id__212=51553480; CPTK_212=1573112941; CPID_212=51553480; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1702436190; ab_sr=1.0.1_ZjFmZjQ2NmY2NDI3NDg4OThiNTZmYjEzNTAyZTQyMzgxNDcxOTkyNTdmNzVkNGFmZWM1MzI1YWZjYzdkNzZhNTUwMWZkMTQ3MmUxZWU1MjBkZTMyNDY2M2MyOGYzZDk4ZTQzYmU4MTQwNTVjNWMyN2I3MmVlZmFjMDRiYjZlOTFhNGM2MDJjYzYwZDNkODkyN2E4M2RkMWU3ZmY4YjFiMA==; BDUSS_BFESS=5Lb1owUVdYZVlicHgyYUhjNXF-anU5RXpNTkZkbGJSV0FPfnZpYmN0UUhMNDVsRVFBQUFBJCQAAAAAAAAAAAEAAAD2HZUDd2FuZ3lhb2RyZWFtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeiZmUHomZlMn; RT="z=1&dm=baidu.com&si=1ddc03b8-cc38-453c-9543-eac11390ca3c&ss=lq36jt1o&sl=1&tt=1a6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2yu&ul=87z"'''

def main():
    if not os.path.exists("temp"):
        os.mkdir("temp")


    conn = pymysql.connect(host=os.getenv("MYSQL_HOST"),
                           user=os.getenv("MYSQL_USER"),
                           port=int(os.getenv("MYSQL_PORT")),
                           password=os.getenv("MYSQL_PASSWORD"),
                           database="baidu_index_db",
                           cursorclass=pymysql.cursors.DictCursor)
    
    with conn:
        cursor = conn.cursor()
        sql = "select * from base"
        cursor.execute(sql)
        result = cursor.fetchall()
        # get_data
        sample = random.choice(result)
        indeices = get_search_index(
                keywords_list=[[sample["key_field"]]],
                start_date="2020-01-01",
                end_date="2022-01-01",
                cookies=cookie)
        for index in indeices:
            print(index)


if __name__ == "__main__":
    main()


