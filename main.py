import os
import json
import random

import pymysql
from qdata import QdataError
from pymysql.cursors import DictCursor
from qdata.baidu_index import get_search_index


def main():
    if not os.path.exists("temp"):
        os.mkdir("temp")

    # get cookie
    try:
        with open("temp/cookie", "r") as cookie_f:
            cookie = cookie_f.read()
    except FileNotFoundError as e:
        raise Exception("没有找到cookie文件，请创建cookie后再执行程序！")

    connection = pymysql.connect(host=os.getenv("MYSQL_HOST"),
                                 user=os.getenv("MYSQL_USER"),
                                 port=int(os.getenv("MYSQL_PORT")),
                                 password=os.getenv("MYSQL_PASSWORD"),
                                 database="baidu_index_db",
                                 cursorclass=DictCursor)

    with connection as conn:
        cursor = conn.cursor()
        sql = "select * from base where status_code is null"
        cursor.execute(sql)
        results: tuple = cursor.fetchall()
        # get data
        update_items = []
        update_sql = f"UPDATE base SET status_code=%s where id=%s"
        try:
            for item in results:
                target_keyword = item["key_field"]
                try:
                    indices = get_search_index(
                        keywords_list=[[target_keyword]],
                        start_date="2022-02-01",
                        end_date="2022-02-01",
                        cookies=cookie)
                    for index in indices:
                        # TODO 需要将数据保存下来
                        print(index)
                    update_items.append(("READY", item['id']))
                except QdataError as e:
                    update_items.append((e.real_code, item['id']))
        finally:
            cursor.executemany(update_sql, update_items)


if __name__ == "__main__":
    main()
