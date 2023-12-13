import os
import json
import random

import pymysql
from qdata.baidu_index import get_search_index



def main():
    if not os.path.exists("temp"):
        os.mkdir("temp")

    # get cookie
    with open("temp/cookie", "r") as conf_f:
        cookie = conf_f.read().replace("\n", "")


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


