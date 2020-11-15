# -*- coding: utf-8 -*-
# @Time : 2020/10/18 23:46
# @Author : wianwu
# @Software: PyCharm 
'''官方文档：https://api.mongodb.com/python/current/api/pymongo/collection.html
    菜鸟教程：https://www.runoob.com/mongodb/mongodb-tutorial.html
    #条件查询query菜鸟教程：https://www.runoob.com/mongodb/mongodb-query.html
'''

import pymongo



def connet_db(url):
    '''
    连接数据库的基本操作：
    '''
    url = "mongodb://localhost:27017/"
    myclient = pymongo.MongoClient(url)  #创建一个客户端
    mydb = myclient["database"] #选择一个数据库
    collection = mydb["collection"] #选择一个集合

    return collection


'''创建数据库'''
def create_db():
    '''
    创建一个集合
    在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。
    :return:
    '''
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["runoobdb"]  # Xianwu:连接数据库

        mycol = mydb["sites"]  # Xianwu:sites:集合名称

        #插入文档：使用
        mydict = {"new_collction": "create sucessful"}
        x = mycol.insert_one(mydict)
        print(x)
    except:
        print("create erro")


def exist_db(db_name):
    '''

    判断数据库是否存在
    list_database_names()

    判断集合是否存在
    collection_names()返回数据库列表
    :return:
    '''
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    dblist = myclient.list_database_names()
    # dblist = myclient.database_names() python3.7前的

    if db_name in dblist:
        print("数据库已存在！")
        return myclient[db_name]
    else:
        return None




'''插入集合'''
def insert_one_doc():
    '''
    插入一条数据
    :return:
    '''

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # Xianwu:连接
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    mydict = {"name": "RUNOOB",  # Xianwu:要插入的数据
              "alexa": "10000",
              "url": "https://www.runoob.com"}
    x = mycol.insert_one(mydict)
    print(x)
    print(x.inserted_id)  #返回id字段

def insert_many_doc():
    '''插入多个文档
    使用列表插入多个文档insert_many(doc_list)
    '''
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    mylist = [
        {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ]
    x = mycol.insert_many(mylist)
    # 输出插入的所有文档对应的 _id 值
    print(x.inserted_ids)

def insert_byid():
    '''
    指定id插入
    每一个文档都有个 '_id:n' 的键值
    :return:
    '''

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["site2"]

    mylist = [
        {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
        {"_id": 2, "name": "Google", "address": "Google 搜索"},
        {"_id": 3, "name": "Facebook", "address": "脸书"},
        {"_id": 4, "name": "Taobao", "address": "淘宝"},
        {"_id": 5, "name": "Zhihu", "address": "知乎"}
    ]

    x = mycol.insert_many(mylist)
    # 输出插入的所有文档对应的 _id 值
    print(x.inserted_ids)


def find_doc():
    '''
    查询文档find_one
    查询最新的一条文档
    find_one()
    '''
    # 查询一个文档
    myclient = pymongo.MongoClient("mongodb://localhost:27017/") #连接
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    x = mycol.find_one()

    print(x)

def fine_all():
    #查询所有find()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    for x in mycol.find():
        print(x)

def find_limt_field():
    '''
    find()
    第一个参数为条件，第二个参数为是否显示（也就是说是否查找）
    # 参数设置0为不显示，1为显示，如果只设置0则其他为1 ， 反之同理
    # 查询指定字段的数据
    :return:
    '''

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    # 参数设置0为不显示，1为显示，如果只设置0则其他为1 ， 反之同理
    for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
        print(x)


def fine_by_partdoc():
    '''
    通过doc中的某一个键值对来查询真个doc
    :return:
    '''

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    myquery = {"name": "RUNOOB"}

    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

##以下实例用于读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} :
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"name": {"$gt": "H"}}
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

##正则表达式：以下实例用于读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"} :
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["runoobdb"]
# mycol = mydb["sites"]
#
# myquery = {"name": {"$regex": "^R"}}
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#     print(x)

def fine_limit_number():
    '''
    查找有限条字段limit(number)
    :return:
    '''
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    myresult = mycol.find().limit(3)

    # 输出结果
    for x in myresult:
        print(x)

def update_one_doc():
    '''修改文档'''
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    myquery = {"alexa": "10000"} #对应文档的键值
    newvalues = {"$set": {"alexa": "12345"}} #修改格式

    mycol.update_one(myquery, newvalues)

    # 输出修改后的  "sites"  集合
    for x in mycol.find():
        print(x)

def update_many_doc():
    '''
    修改多条记录 改变查询条件
    :return:
    '''
    #修改多条记录
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    myquery = {"name": {"$regex": "^F"}}   #正则表达式 嵌入query条件中
    newvalues = {"$set": {"alexa": "123"}}

    x = mycol.update_many(myquery, newvalues)

    print(x.modified_count, "文档已修改")

def sort_doc():
    '''排序
    #sort第一个是表示用文档的那个值进行排序，输入值对应的键名，第二个参数表示用肾虚还是降序
    '''
    # ##升序
    # # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # # mydb = myclient["runoobdb"]
    # # mycol = mydb["sites"]
    # #
    # # mydoc = mycol.find().sort("alexa")
    # # for x in mydoc:
    # #     print(x)
    #
    #降序
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    mydoc = mycol.find().sort("alexa", -1) #sort第一个是表示用文档的那个值进行排序，输入值对应的键名，第二个参数表示用肾虚还是降序
    # for x in mydoc:
    #     print(x)

def delete_one_doc_bypartdoc():
    '''删除文档
    通过文档的某个键值对来删除整个文档
    '''
    # 删除单个
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    myquery = {"name": "Taobao"} #条件

    mycol.delete_one(myquery)

    # 删除后输出
    for x in mycol.find():
        print(x)
def delete_manydoc_bypartdoc():
    '''
    清空整个集合
    :return:
    '''
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["sites"]

    myquery = {}
    x = mycol.delete_many(myquery)  #全部清空

    print(x.deleted_count, "个文档已删除")

def drop_collction():
    # 删除集合
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["runoobdb"]
    mycol = mydb["site2"]

    ret = mycol.drop()
    if ret :
        print("已经删除")

if __name__ == '__main__':
    pass