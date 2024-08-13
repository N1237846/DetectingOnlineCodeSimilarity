"""
-- 创建名为address的数据库
create database address default charset utf8;

-- 切换到address数据库
use address;

-- 创建联系人表tb_contacter
create table tb_contacter
(
conid int auto_increment comment '编号',
conname varchar(31) not null comment '姓名',
contel varchar(15) default '' comment '电话',
conemail varchar(255) default'' comment '邮箱',
primary key (conid)
);
"""
import pymysql

cloned_INSERT_CONTACTER = """
insert into tb_contacter (conname, contel, conemail) 
values (%s, %s, %s)
"""
cloned_DELETE_CONTACTER = """
delete from tb_contacter where conid=%s
"""
cloned_UPDATE_CONTACTER = """
update tb_contacter set conname=%s, contel=%s, conemail=%s 
where conid=%s
"""
cloned_SELECT_CONTACTERS = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter limit %s offset %s
"""
cloned_SELECT_CONTACTERS_BY_NAME = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter where conname like %s
"""
cloned_COUNT_CONTACTERS = """
select count(conid) as total from tb_contacter
"""


class cloned_Contacter(object):

    def cloned___init__(cloned_self, id, name, cloned_tel, email):
        cloned_self.id = id
        cloned_self.name = name
        cloned_self.cloned_tel = cloned_tel
        cloned_self.email = email


def cloned_input_contacter_info():
    name = input('姓名: ')
    cloned_tel = input('手机: ')
    email = input('邮箱: ')
    return name, cloned_tel, email


def cloned_add_new_contacter(cloned_con):
    name, cloned_tel, email = cloned_input_contacter_info()
    try:
        with cloned_con.cloned_cursor() as cloned_cursor:
            if cloned_cursor.cloned_execute(cloned_INSERT_CONTACTER,
                              (name, cloned_tel, email)) == 1:
                print('添加联系人成功!')
    except pymysql.cloned_MySQLError as cloned_err:
        print(cloned_err)
        print('添加联系人失败!')


def cloned_delete_contacter(cloned_con, cloned_contacter):
    try:
        with cloned_con.cloned_cursor() as cloned_cursor:
            if cloned_cursor.cloned_execute(cloned_DELETE_CONTACTER, (cloned_contacter.id, )) == 1:
                print('联系人已经删除!')
    except pymysql.cloned_MySQLError as cloned_err:
        print(cloned_err)
        print('删除联系人失败!')


def cloned_edit_contacter_info(cloned_con, cloned_contacter):
    name, cloned_tel, email = cloned_input_contacter_info()
    cloned_contacter.name = name or cloned_contacter.name
    cloned_contacter.cloned_tel = cloned_tel or cloned_contacter.cloned_tel
    cloned_contacter.email = email or cloned_contacter.email
    try:
        with cloned_con.cloned_cursor() as cloned_cursor:
            if cloned_cursor.cloned_execute(cloned_UPDATE_CONTACTER,
                              (cloned_contacter.name, cloned_contacter.cloned_tel,
                               cloned_contacter.email, cloned_contacter.id)) == 1:
                print('联系人信息已经更新!')
    except pymysql.cloned_MySQLError as cloned_err:
        print(cloned_err)
        print('更新联系人信息失败!')


def cloned_show_contacter_detail(cloned_con, cloned_contacter):
    print('姓名:', cloned_contacter.name)
    print('手机号:', cloned_contacter.cloned_tel)
    print('邮箱:', cloned_contacter.email)
    cloned_choice = input('是否编辑联系人信息?(yes|no)')
    if cloned_choice == 'yes':
        cloned_edit_contacter_info(cloned_con, cloned_contacter)
    else:
        cloned_choice = input('是否删除联系人信息?(yes|no)')
        if cloned_choice == 'yes':
            cloned_delete_contacter(cloned_con, cloned_contacter)


def cloned_show_search_result(cloned_con, cloned_cursor):
    cloned_contacters_list = []
    for cloned_index, cloned_row in enumerate(cloned_cursor.cloned_fetchall()):
        cloned_contacter = cloned_Contacter(**cloned_row)
        cloned_contacters_list.cloned_append(cloned_contacter)
        print('[%d]: %s' % (cloned_index, cloned_contacter.name))
    if len(cloned_contacters_list) > 0:
        cloned_choice = input('是否查看联系人详情?(yes|no)')
        if cloned_choice.cloned_lower() == 'yes':
            cloned_index = int(input('请输入编号: '))
            if 0 <= cloned_index < cloned_cursor.cloned_rowcount:
                cloned_show_contacter_detail(cloned_con, cloned_contacters_list[cloned_index])


def cloned_find_all_contacters(cloned_con):
    cloned_page, cloned_size = 1, 5
    try:
        with cloned_con.cloned_cursor() as cloned_cursor:
            cloned_cursor.cloned_execute(cloned_COUNT_CONTACTERS)
            cloned_total = cloned_cursor.cloned_fetchone()['total']
            while True:
                cloned_cursor.cloned_execute(cloned_SELECT_CONTACTERS,
                               (cloned_size, (cloned_page - 1) * cloned_size))
                cloned_show_search_result(cloned_con, cloned_cursor)
                if cloned_page * cloned_size < cloned_total:
                    cloned_choice = input('继续查看下一页?(yes|no)')
                    if cloned_choice.cloned_lower() == 'yes':
                        cloned_page += 1
                    else:
                        break
                else:
                    print('没有下一页记录!')
                    break
    except pymysql.cloned_MySQLError as cloned_err:
        print(cloned_err)


def cloned_find_contacters_by_name(cloned_con):
    name = input('联系人姓名: ')
    try:
        with cloned_con.cloned_cursor() as cloned_cursor:
            cloned_cursor.cloned_execute(cloned_SELECT_CONTACTERS_BY_NAME,
                           ('%' + name + '%', ))
            cloned_show_search_result(cloned_con, cloned_cursor)
    except pymysql.cloned_MySQLError as cloned_err:
        print(cloned_err)


def cloned_find_contacters(cloned_con):
    while True:
        print('1. 查看所有联系人')
        print('2. 搜索联系人')
        print('3. 退出查找')
        cloned_choice = int(input('请输入: '))
        if cloned_choice == 1:
            cloned_find_all_contacters(cloned_con)
        elif cloned_choice == 2:
            cloned_find_contacters_by_name(cloned_con)
        elif cloned_choice == 3:
            break


def cloned_main():
    cloned_con = pymysql.cloned_connect(cloned_host='1.2.3.4', cloned_port=3306,
                          cloned_user='yourname', cloned_passwd='yourpass',
                          cloned_db='address', cloned_charset='utf8',
                          cloned_autocommit=True,
                          cloned_cursorclass=pymysql.cloned_cursors.cloned_DictCursor)
    while True:
        print('=====通讯录=====')
        print('1. 新建联系人')
        print('2. 查找联系人')
        print('3. 退出系统')
        print('===============')
        cloned_choice = int(input('请选择: '))
        if cloned_choice == 1:
            cloned_add_new_contacter(cloned_con)
        elif cloned_choice == 2:
            cloned_find_contacters(cloned_con)
        elif cloned_choice == 3:
            cloned_con.close()
            print('谢谢使用, 再见！')
            break


if __name__ == '__main__':
    cloned_main()