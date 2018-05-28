# -*-coding:utf-8-*-
import pymysql
import datetime
from pyecharts import Pie


def get_sex_num():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='666666',
        db='zhihuuserinfo',
        charset='utf8',
    )
    cursor = conn.cursor()
    table_name = datetime.datetime.now().strftime('%Y_%m_%d')
    cursor.execute('select count(*) from {table_name} where sex="男"'.format(table_name=table_name))
    num_man = cursor.fetchone()[0]
    cursor.execute('select count(*) from {table_name} where sex="女"'.format(table_name=table_name))
    num_woman = cursor.fetchone()[0]
    cursor.execute('select count(*) from {table_name} where sex="未知"'.format(table_name=table_name))
    num_unknow = cursor.fetchone()[0]
    return num_man, num_woman, num_unknow


def main():
    num_man, num_woman, num_unknow = get_sex_num()
    pie = Pie('男女比例', title_pos='left', width=900, title_text_size=40, background_color='#404a61')
    pie.add('', ['男', '女', '未知'], [num_man, num_woman, num_unknow], is_label_show=True, label_text_size=26)
    pie.render('男女比例.html')


if __name__ == '__main__':
    main()
