# README
# 定向词汇数目查询系统

定向词汇数目查询系统 是基于python语言开发的查询系统，方便确定文章中关键字等。使用redis 对数据进行存储，准许在程序启动过程中存储多组数目数据。方便纵向文章对比。

同时支持word文档检索。

## 运行环境

python 3.7

- python-redis
- python-sys库
- python-docx库

redis-server

Ubuntu18.04

### 参考命令

````bash
apt-get install redis

systemctl start redis
systemctl stop redis
````

````bash
#anaconda中安装方式
pip uninstall redis
pip install redis
````



### python-redis库简介

参考网址（[Python redis 使用介绍 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/python-redis-intro.html)）

````python
#调用
import redis
#注意：官方python中自带redis库，Anaconda中python有该库但指令不全。

#连接测试
r = redis.StrictRedis(host='localhost', port=6379)
r.set('foo', 'bar')
print(r.get('foo'))

#redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)  


#String
r.set(name, value, ex=None, px=None, nx=False, xx=False)
#ex - 过期时间（秒）
#px - 过期时间（毫秒）
#nx - 如果设置为True，则只有name不存在时，当前set操作才执行
#xx - 如果设置为True，则只有name存在时，当前set操作才执行
r.setnx(name, value)#设置值，只有name不存在时，执行设置操作（添加）
r.setex(name, time, value)#设置值。time - 过期时间（数字秒 或 timedelta对象）
psetex(name, time_ms, value)#设置值。time_ms - 过期时间（数字毫秒 或 timedelta对象）
getset(name, value)#设置新值并获取原来的值

#批量化处理
r.mset(*args, **kwargs)#批量设置值
mget(keys, *args)#批量获取

#hash
r.hset(name, key, value)
#name对应的hash中设置一个键值对（不存在，则创建；否则，修改）name - redis的name;
#key - name对应的hash中的key;value - name对应的hash中的value
r.hmset(name, mapping)#在name对应的hash中批量设置键值对。
#name - redis的name,mapping - 字典，如：{'k1':'v1', 'k2': 'v2'}
r.hmget(name, keys, *args)#在name对应的hash中获取多个key的值
r.hgetall(name)#获取name对应hash的所有键值
r.hlen(name)#获取name对应的hash中键值对的个数
r.hkeys(name)#获取name对应的hash中所有的key的值
r.hexists(name, key)#检查 name 对应的 hash 是否存在当前传入的 key
````

### python-docx库简介

本程序中用于读取word文档。该库可以允许使用python操作word文档，包括居中，间距等功能

参考网址[Python docx库用法示例分析](https://www.jb51.net/article/156389.htm)

````python
#安装
pip install python-docx

from docx import Document
document = Document('test.docx')#导入word文档
document.save('test.docx')#保存

#调整文本位置格式为居中：
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
document = Document('test.docx')
paragraph = document.add_paragraph('123')
paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
document.save('test.docx')
````

python-docx中文文档[python-docx库中文说明 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/338893674)

## 作品功能

### 主要代码构成

````
nosqlproject.py#主代码，连接redis
wordCount.py#去除无意义符号等
wordcount.py#读取word文档
````

### NoSql技术

​	redis

#### redis hash设定

hash自定名称：word1 num1	word2 num2

允许插入多个hash表以在程序运行过程中存储多个文档数据

## 参考

### 源码

[源码所放](./sources)

### 文献

[基于NoSQL技术的文档检索系统设计与实现](.\docs\基于NoSQL技术的文档检索系统设计与实现.pdf)

